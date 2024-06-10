from killb.api_requests import ApiRequests
from killb.types.quotations import CreateQuotation, CreateQuotationResponse, SimulateQuotationResponse


class Quotation:
    """
        Quotation class to interact with the KillB API for creating and simulating quotations.

        Attributes
        ----------
        api_requests : ApiRequests
            An instance of the ApiRequests class used for making authenticated API requests.

        Methods
        -------
        create(data: CreateQuotation) -> CreateQuotationResponse
            Creates a new quotation based on the provided data.
        simulate(data: CreateQuotation) -> SimulateQuotationResponse
            Simulates a quotation based on the provided data without actually creating it.
    """
    def __init__(self, api_requests: ApiRequests):
        """
            Initializes the Quotation object with the given api_requests instance.

            Parameters
            ----------
            api_requests : ApiRequests
                An instance of the ApiRequests class used for making authenticated API requests.
        """
        self.api_requests = api_requests

    def create(self, data: CreateQuotation) -> CreateQuotationResponse:
        """
            Creates a new quotation based on the provided data.

            Parameters
            ----------
            data : CreateQuotation
                The data required to create a quotation, including currencies, amount, and methods.

            Returns
            -------
            CreateQuotationResponse
                The response from the API as a dictionary containing the created quotation details.

            Example
            -------
            quotation_data = {
                "fromCurrency": FromCurrency.MXN,
                "toCurrency": ToCurrency.USDC,
                "amount": 1000,
                "amountIsToCurrency": False,
                "cashInMethod": CashInMethod.SPEI,
                "cashOutMethod": CashOutMethod.POLYGON,
                "skipOrder": None
            }

            response = quotation.create(quotation_data)
            print(response)
        """
        return self.api_requests.request(method="POST", endpoint="quotations", json=data)

    def simulate(self, data: CreateQuotation) -> SimulateQuotationResponse:
        """
           Simulates a quotation based on the provided data without actually creating it.

           Parameters
           ----------
           data : CreateQuotation
               The data required to simulate a quotation, including currencies, amount, and methods.

           Returns
           -------
           SimulateQuotationResponse
               The response from the API as a dictionary containing the simulated quotation details.

           Example
           -------
           quotation_data = {
               "fromCurrency": FromCurrency.MXN,
               "toCurrency": ToCurrency.USDC,
               "amount": 1000,
               "amountIsToCurrency": False,
               "cashInMethod": CashInMethod.SPEI,
               "cashOutMethod": CashOutMethod.POLYGON,
               "skipOrder": None
           }

           response = quotation.simulate(quotation_data)
           print(response)
        """
        return self.api_requests.request(method="POST", endpoint="quotations/simulation", json=data)
