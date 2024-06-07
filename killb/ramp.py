from killb.api_requests import ApiRequests
from killb.types.ramps import CreateRampResponse, CreateRampData, GetRampQueryResponse, GetRampQuery
from urllib.parse import urlencode


class Ramps:
    def __init__(self, api_requests: ApiRequests):
        self.api_requests = api_requests

    def create(self, data: CreateRampData) -> CreateRampResponse:
        return self.api_requests.request(method="POST", endpoint="ramps", json=data)

    def get_by_query(self, data: GetRampQuery) -> GetRampQueryResponse:
        query_string = urlencode(data)
        return self.api_requests.request(method="GET", endpoint=f"ramps?{query_string}")
