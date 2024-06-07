from killb.api_requests import ApiRequests
from killb.types.quotations import CreateQuotation, CreateQuotationResponse, SimulateQuotationResponse


class Quotation:
    def __init__(self, api_requests: ApiRequests):
        self.api_requests = api_requests

    def create(self, data: CreateQuotation) -> CreateQuotationResponse:
        return self.api_requests.request(method="POST", endpoint="quotations", json=data)

    def simulate(self, data: CreateQuotation) -> SimulateQuotationResponse:
        return self.api_requests.request(method="POST", endpoint="quotations/simulation", json=data)
