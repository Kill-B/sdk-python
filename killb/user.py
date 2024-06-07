from killb.api_requests import ApiRequests
from killb.types.user import UserCreateData, UserCreateResponse, PersonData, CompanyData, GetUserByQuery
from typing import Union
from urllib.parse import urlencode


class User:
    def __init__(self, api_requests: ApiRequests):
        self.api_requests = api_requests

    def create(self, data: UserCreateData) -> UserCreateResponse:
        return self.api_requests.request(method="POST", endpoint="users", json=data)

    def update(self, data: Union[PersonData, CompanyData], user_id: str) -> UserCreateResponse:
        return self.api_requests.request(method="PATCH", endpoint=f"users/{user_id}", json=data)

    def get_by_query(self, data: GetUserByQuery):
        query_string = urlencode(data)
        return self.api_requests.request(method="GET", endpoint=f"users?{query_string}")
