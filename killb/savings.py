from killb.api_requests import ApiRequests
from killb.types.savings import SavingsCreateResponse, SavingsWithdrawalData, SavingsWithdrawalReturn, \
    SavingsGetTransactionReturn, SavingsGetTransactions, SavingsGetBalanceReturn, SavingsGetDepositInstructions, \
    SavingsGetDepositInstructionsReturn
from urllib.parse import urlencode


class Savings:
    """
        Savings class to interact with the KillB API for managing savings accounts.

        Attributes
        ----------
        api_requests : ApiRequests
            An instance of the ApiRequests class used for making authenticated API requests.

        Methods
        -------
        create(user_id: str) -> SavingsCreateResponse
            Creates a new savings account for the specified user.

        get(user_id: str) -> SavingsCreateResponse
            Retrieves the details of the savings account associated with the specified user.

        withdrawal(data: SavingsWithdrawalData) -> SavingsWithdrawalReturn
            Initiates a withdrawal from the savings account based on the provided withdrawal data.

        get_transactions(data: SavingsGetTransactions) -> SavingsGetTransactionReturn
            Retrieves transactions associated with the savings account based on the provided query parameters.

        get_balance(savings_account_id: str) -> SavingsGetBalanceReturn
            Retrieves the balance of the specified savings account.

        get_deposit_instructions(data: SavingsGetDepositInstructions) -> SavingsGetDepositInstructionsReturn
            Retrieves deposit instructions for the specified savings account.

        get_wallet_address(savings_account_id: str)
            Retrieves the wallet address for the specified savings account.
    """
    def __init__(self, api_requests: ApiRequests):
        """
            Initializes the Savings object with the given api_requests instance.

            Parameters
            ----------
            api_requests : ApiRequests
                An instance of the ApiRequests class used for making authenticated API requests.
        """
        self.api_requests = api_requests

    def create(self, user_id: str) -> SavingsCreateResponse:
        """
            Creates a new savings account for the specified user.

            Parameters
            ----------
            user_id : str
                The ID of the user for whom the savings account is to be created.

            Returns
            -------
            SavingsCreateResponse
                The response from the API containing the details of the created savings account.
        """
        return self.api_requests.request(method="POST", endpoint="savings", json={"UserId": user_id})

    def get(self, user_id: str) -> SavingsCreateResponse:
        """
            Retrieves the details of the savings account associated with the specified user.

            Parameters
            ----------
            user_id : str
                The ID of the user whose savings account details are to be retrieved.

            Returns
            -------
            SavingsCreateResponse
                The response from the API containing the details of the savings account.
        """
        return self.api_requests.request(method="GET", endpoint=f"savings/{user_id}")

    def withdrawal(self, data: SavingsWithdrawalData) -> SavingsWithdrawalReturn:
        """
            Initiates a withdrawal from the savings account based on the provided withdrawal data.

            Parameters
            ----------
            data : SavingsWithdrawalData
                The data required to initiate the withdrawal, including source, destination, amount, and optional comment.

            Returns
            -------
            SavingsWithdrawalReturn
                The response from the API containing the details of the withdrawal transaction.
        """
        return self.api_requests.request(method="POST", endpoint="savings/withdrawal", json=data)

    def get_transactions(self, data: SavingsGetTransactions) -> SavingsGetTransactionReturn:
        """
            Retrieves transactions associated with the savings account based on the provided query parameters.

            Parameters
            ----------
            data : SavingsGetTransactions
                The query parameters to filter transactions, such as limit, page, ID, destination account ID, origin account ID, user ID, and type.

            Returns
            -------
            SavingsGetTransactionReturn
                The response from the API containing the list of transactions and total count.
        """
        query_string = urlencode(data)
        return self.api_requests.request(method="GET", endpoint=f"savings/transactions?{query_string}")

    def get_balance(self, savings_account_id: str) -> SavingsGetBalanceReturn:
        """
            Retrieves the balance of the specified savings account.

            Parameters
            ----------
            savings_account_id : str
                The ID of the savings account whose balance is to be retrieved.

            Returns
            -------
            SavingsGetBalanceReturn
                The response from the API containing the balance of the savings account.
        """
        return self.api_requests.request(method="GET", endpoint=f"savings/{savings_account_id}/balance")

    def get_deposit_instructions(self, data: SavingsGetDepositInstructions) -> SavingsGetDepositInstructionsReturn:
        """
            Retrieves deposit instructions for the specified savings account.

            Parameters
            ----------
            data : SavingsGetDepositInstructions
                The data containing the savings account ID and the type of deposit instructions to retrieve.

            Returns
            -------
            SavingsGetDepositInstructionsReturn
                The response from the API containing the deposit instructions.
        """
        return self.api_requests.request(method="GET",
                                         endpoint=f"savings/{data.get('savings_account_id')}/deposit-instructions/{data.get('type')}")

    def get_wallet_address(self, savings_account_id: str):
        """
            Retrieves the wallet address for the specified savings account.

            Parameters
            ----------
            savings_account_id : str
                The ID of the savings account for which to retrieve the wallet address.

            Returns
            -------
            Any
                The wallet address associated with the specified savings account.
        """
        return self.api_requests.request(method="GET", endpoint=f"savings/{savings_account_id}/crypto-deposit-instructions")
