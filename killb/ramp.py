from killb.api_requests import ApiRequests
from killb.types.ramps import CreateRampResponse, CreateRampData, GetRampQueryResponse, GetRampQuery
from urllib.parse import urlencode


class Ramps:
    """
        Ramps class to interact with the KillB API for creating and querying ramps.

        Attributes
        ----------
        api_requests : ApiRequests
            An instance of the ApiRequests class used for making authenticated API requests.

        Methods
        -------
        create(data: CreateRampData) -> CreateRampResponse
            Creates a new ramp based on the provided data.
        get_by_query(data: GetRampQuery) -> GetRampQueryResponse
            Retrieves ramps based on the provided query parameters.
    """
    def __init__(self, api_requests: ApiRequests):
        """
            Initializes the Ramps object with the given api_requests instance.

            Parameters
            ----------
            api_requests : ApiRequests
                An instance of the ApiRequests class used for making authenticated API requests.
        """
        self.api_requests = api_requests

    def create(self, data: CreateRampData) -> CreateRampResponse:
        """
            Creates a new ramp based on the provided data.

            Parameters
            ----------
            data : CreateRampData
                The data required to create a ramp, including quotation ID, user ID, account ID, and optional refund instructions.

            Returns
            -------
            CreateRampResponse
                The response from the API as a dictionary containing the created ramp details.

            Example
            -------
            ramp_data = {
                "quotationId": "12345",
                "userId": "user123",
                "accountId": "account123",
                "refundInstructions": {
                    "network": "ERC20",
                    "address": "0x...",
                    "asset": "USDC"
                }
            }

            response = ramps.create(ramp_data)
            print(response)
        """
        return self.api_requests.request(method="POST", endpoint="ramps", json=data)

    def get_by_query(self, data: GetRampQuery) -> GetRampQueryResponse:
        """
            Retrieves ramps based on the provided query parameters.

            Parameters
            ----------
            data : GetRampQuery
                The query parameters to filter ramps, such as user ID, account ID, active status, type, limit, and offset.

            Returns
            -------
            GetRampQueryResponse
                The response from the API as a dictionary containing a list of ramps and the total count.

            Example
            -------
            query_params = {
                "userId": "user123",
                "active": True,
                "limit": 10,
                "offset": 0
            }

            response = ramps.get_by_query(query_params)
            print(response)
        """
        query_string = urlencode(data)
        return self.api_requests.request(method="GET", endpoint=f"ramps?{query_string}")
