from killb.api_requests import ApiRequests
from killb.account import Account
from killb.user import User
from killb.quotations import Quotation
from killb.savings import Savings


class Client:
    """
        Client class to interact with the KillB API.

        This class serves as the main entry point to interact with various endpoints of the KillB API. It handles
        authentication and provides access to the Account, User, Quotation, and Savings API endpoints.

        Attributes
        ----------
        api_requests : ApiRequests
            An instance of the ApiRequests class used for making authenticated API requests.
        Account : Account
            An instance of the Account class to interact with account-related API endpoints.
        User : User
            An instance of the User class to interact with user-related API endpoints.
        Quotation : Quotation
            An instance of the Quotation class to interact with quotation-related API endpoints.
        Savings : Savings
            An instance of the Savings class to interact with savings-related API endpoints.

        Methods
        -------
        __init__(environment: str, email: str, password: str, api_key: str = None)
            Initializes the Client with the given credentials and authenticates the user.
    """
    def __init__(self, environment: str, email: str, password: str, api_key: str = None):
        self.api_requests = ApiRequests(environment=environment, email=email, password=password, api_key=api_key)
        self.api_requests.authenticate()
        self.Account = Account(self.api_requests)
        self.User = User(self.api_requests)
        self.Quotation = Quotation(self.api_requests)
        self.Savings = Savings(self.api_requests)
