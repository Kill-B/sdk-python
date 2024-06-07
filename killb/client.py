from killb.api_requests import ApiRequests
from killb.account import Account
from killb.user import User
from killb.quotations import Quotation
from killb.savings import Savings


class Client:
    def __init__(self, environment: str, email: str, password: str, api_key: str = None):
        self.api_requests = ApiRequests(environment=environment, email=email, password=password, api_key=api_key)
        self.api_requests.authenticate()
        self.Account = Account(self.api_requests)
        self.User = User(self.api_requests)
        self.Quotation = Quotation(self.api_requests)
        self.Savings = Savings(self.api_requests)
