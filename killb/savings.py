from killb.api_requests import ApiRequests
from killb.types.savings import SavingsCreateResponse, SavingsWithdrawalData, SavingsWithdrawalReturn, \
    SavingsGetTransactionReturn, SavingsGetTransactions, SavingsGetBalanceReturn, SavingsGetDepositInstructions, \
    SavingsGetDepositInstructionsReturn
from urllib.parse import urlencode


class Savings:
    def __init__(self, api_requests: ApiRequests):
        self.api_requests = api_requests

    def create(self, user_id: str) -> SavingsCreateResponse:
        return self.api_requests.request(method="POST", endpoint="savings", json={"UserId": user_id})

    def get(self, user_id: str) -> SavingsCreateResponse:
        return self.api_requests.request(method="GET", endpoint=f"savings/{user_id}")

    def withdrawal(self, data: SavingsWithdrawalData) -> SavingsWithdrawalReturn:
        return self.api_requests.request(method="POST", endpoint="savings/withdrawal", json=data)

    def get_transactions(self, data: SavingsGetTransactions) -> SavingsGetTransactionReturn:
        query_string = urlencode(data)
        return self.api_requests.request(method="GET", endpoint=f"savings/transactions?{query_string}")

    def get_balance(self, savings_account_id: str) -> SavingsGetBalanceReturn:
        return self.api_requests.request(method="GET", endpoint=f"savings/{savings_account_id}/balance")

    def get_deposit_instructions(self, data: SavingsGetDepositInstructions) -> SavingsGetDepositInstructionsReturn:
        return self.api_requests.request(method="GET",
                                         endpoint=f"savings/{data.get('savings_account_id')}/deposit-instructions/{data.get('type')}")

    def get_wallet_address(self, savings_account_id: str):
        return self.api_requests.request(method="GET", endpoint=f"savings/{savings_account_id}/crypto-deposit-instructions")
