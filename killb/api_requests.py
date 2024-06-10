import requests as re
from datetime import datetime, timedelta
from killb.exceptions import KillBApiError, AuthenticationError


class ApiRequests:
    def __init__(self, environment: str, email: str, password: str, api_key: str = None):
        self.environment = environment
        self.api_key = api_key
        self.access_token = None
        self.base_url = ''
        self.email = email
        self.password = password
        self.expires_at = 0
        self.token_expiry = None
        self.headers = {"x-api-key": self.api_key,
                        "Authorization": f"Bearer {self.access_token}" if self.access_token else None}

    def get_base_url(self):
        if self.environment == 'SANDBOX':
            self.base_url = 'https://teste-94u93qnn.uc.gateway.dev'
            return self.base_url
        self.base_url = 'http://killb.app/api/v2'
        return self.base_url

    def token_expired(self):
        if not self.token_expiry:
            return True
        return datetime.now() > self.token_expiry

    def request(self, method, endpoint, **kwargs):
        if self.token_expired():
            self.refresh_token()

        url = f"{self.base_url}/{endpoint}"
        response = re.request(method=method, url=url, headers=self.headers, **kwargs)

        if response.status_code == 401:
            raise AuthenticationError("Authentication Failed")
        elif not response.ok:
            raise KillBApiError(f"Error: {response.status_code} - {response.text}")
        
        return response.json()

    def authenticate(self):
        response_auth = re.post(url=f'{self.get_base_url()}/auth/login',
                                data={"email": self.email, "password": self.password}, headers={"x-api-key": self.api_key})
        response = response_auth.json()

        if response_auth.status_code >= 200:
            self.access_token = response["accessToken"]
            self.headers["Authorization"] = f"Bearer {self.access_token}"
            expires_in = response["expiresIn"]
            self.token_expiry = datetime.now() + timedelta(seconds=expires_in)
        else:
            raise AuthenticationError(f"Authentication Failed: {response.text}")

    def refresh_token(self):
        if self.email and self.password:
            self.authenticate()
        else:
            raise AuthenticationError("Cannot refresh token without credentials")
