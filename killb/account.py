from killb.types.account import AccountData, AccountCreateResponse, AccountUpdateData
from killb.api_requests import ApiRequests


class Account:
    def __init__(self, api_requests: ApiRequests):
        self.api_requests = api_requests

    def create(self, data: AccountData) -> AccountCreateResponse:
        return self.api_requests.request(method="POST", endpoint="accounts", json=data)

    def update(self, account_id: str, data: AccountUpdateData) -> AccountCreateResponse:
        return self.api_requests.request(method="PATCH", endpoint=f"accounts/{account_id}", json=data)

    def get_by_id(self, account_id: str) -> AccountCreateResponse:
        return self.api_requests.request(method="GET", endpoint=f"accounts/{account_id}")

    def get_by_user(self, user_id: str) -> AccountCreateResponse:
        return self.api_requests.request(method="GET", endpoint=f"accounts/{user_id}")
