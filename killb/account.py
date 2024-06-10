from killb.types.account import AccountData, AccountCreateResponse, AccountUpdateData
from killb.api_requests import ApiRequests


class Account:
    """
        A class to interact with the Account endpoints of the KillB API.

        Attributes
        ----------
        api_requests : APIRequests
            An instance of the APIRequests class to handle API requests.

        Methods
        -------
        create(data: AccountData) -> AccountCreateResponse:
            Creates a new account.
        update(account_id: str, data: AccountUpdateData) -> AccountCreateResponse:
            Updates an existing account.
        get_by_id(account_id: str) -> AccountCreateResponse:
            Retrieves an account by its ID.
        get_by_user(user_id: str) -> AccountCreateResponse:
            Retrieves accounts associated with a user ID.
    """
    def __init__(self, api_requests: ApiRequests):
        """
            Constructs all the necessary attributes for the Account object.

            Parameters
            ----------
            api_requests : APIRequests
                An instance of the APIRequests class to handle API requests.
        """
        self.api_requests = api_requests

    def create(self, data: AccountData) -> AccountCreateResponse:
        """
            Creates a new account.

            Parameters
            ----------
            data : AccountData
                The account creation data. The structure depends on the account type.

                - For a PSE account:
                    {
                        "type": "pse",
                        "userId": "user-id-123",
                        "data": {
                            "firstName": "John",
                            "middleName": "A",
                            "lastName": "Doe",
                            "companyName": "Example Corp",
                            "email": "john.doe@example.com",
                            "phone": "1234567890",
                            "accountNumber": "123456789",
                            "bankCode": "001",
                            "type": "savings",
                            "countryCode": "US",
                            "document": {
                                "type": "PASSPORT",
                                "number": "A1234567",
                                "issuedCountryCode": "US",
                                "expeditionDate": "2020-01-01"
                            }
                        },
                        "externalId": "external-id-123"
                    }

                - For a Wallet account:
                    {
                        "type": "wallet",
                        "userId": "user-id-456",
                        "data": {
                            "firstName": "John",
                            "middleName": "A",
                            "lastName": "Doe",
                            "companyName": "Example Corp",
                            "email": "john.doe@example.com",
                            "phone": "1234567890",
                            "document": {
                                "type": "PASSPORT",
                                "number": "A1234567",
                                "issuedCountryCode": "US",
                                "expeditionDate": "2020-01-01"
                            },
                            "currency": "USDC",
                            "network": "POLYGON",
                            "address": "0x123456789abcdef"
                        },
                        "externalId": "external-id-456"
                    }

                - For a SPEI account:
                    {
                        "type": "spei",
                        "userId": "user-id-789",
                        "data": {
                            "firstName": "John",
                            "middleName": "A",
                            "lastName": "Doe",
                            "companyName": "Example Corp",
                            "email": "john.doe@example.com",
                            "phone": "1234567890",
                            "document": {
                                "type": "PASSPORT",
                                "number": "A1234567",
                                "issuedCountryCode": "US",
                                "expeditionDate": "2020-01-01"
                            },
                            "clabe": "123456789012345678",
                            "clabeType": "type",
                            "bankCode": "001",
                            "countryCode": "US"
                        },
                        "externalId": "external-id-789"
                    }

            Returns
            -------
            AccountCreateResponse
                The response from the API as a dictionary.
        """
        return self.api_requests.request(method="POST", endpoint="accounts", json=data)

    def update(self, account_id: str, data: AccountUpdateData) -> AccountCreateResponse:
        """
            Updates an existing account.

            Parameters
            ----------
            account_id : str
                The ID of the account to update.
            data : Union[PSEAccountUpdate, WalletAccountUpdate, SPEIAccountUpdate]
                The updated account data.

            Returns
            -------
            AccountCreateResponse
                The response from the API as a dictionary.
        """
        return self.api_requests.request(method="PATCH", endpoint=f"accounts/{account_id}", json=data)

    def get_by_id(self, account_id: str) -> AccountCreateResponse:
        """
            Retrieves an account by its ID.

            Parameters
            ----------
            account_id : str
                The ID of the account to retrieve.

            Returns
            -------
            AccountCreateResponse
                The response from the API as a dictionary.
        """
        return self.api_requests.request(method="GET", endpoint=f"accounts/{account_id}")

    def get_by_user(self, user_id: str) -> AccountCreateResponse:
        """
            Retrieves accounts associated with a user ID.

            Parameters
            ----------
            user_id : str
                The ID of the user whose accounts are to be retrieved.

            Returns
            -------
            AccountCreateResponse
                The response from the API as a dictionary.
        """
        return self.api_requests.request(method="GET", endpoint=f"accounts/{user_id}")
