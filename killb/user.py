from killb.api_requests import ApiRequests
from killb.types.user import UserCreateData, UserCreateResponse, PersonData, CompanyData, GetUserByQuery
from typing import Union
from urllib.parse import urlencode


class User:
    """
        A class to interact with the User endpoints of the KillB API V2.

        Attributes:
        ----------
        api_requests : APIRequests
            An instance of the APIRequests class to handle API requests.

        Methods:
        -------
        create(data: dict) -> dict:
            Creates a new user.
        update(data: dict, user_id: str) -> dict:
            Updates an existing user.
        get_by_query(query_params: dict) -> dict:
            Retrieves users based on query parameters.
    """
    def __init__(self, api_requests: ApiRequests):
        """
            Constructs all the necessary attributes for the User object.

            Parameters:
            ----------
            api_requests : APIRequests
                An instance of the APIRequests class to handle API requests.
        """
        self.api_requests = api_requests

    def create(self, data: UserCreateData) -> UserCreateResponse:
        """
            Creates a new user.

            Parameters:
            ----------
            data : UserCreateData
                The user creation data. The structure depends on the user type.

                - For a PERSON type user:
                    {
                        "type": "PERSON",
                        "data": {
                            "firstName": "John",
                            "middleName": "A",
                            "lastName": "Doe",
                            "dateOfBirth": "1990-01-01",
                            "email": "john.doe@example.com",
                            "phone": "1234567890",
                            "address": {
                                "street1": "123 Main St",
                                "street2": "Apt 4",
                                "city": "New York",
                                "state": "NY",
                                "zipCode": "10001",
                                "countryCode": "US"
                            },
                            "document": {
                                "type": "PASSPORT",
                                "number": "A1234567",
                                "issuedCountryCode": "US"
                            }
                        },
                        "externalId": "external-id-123"
                    }

                - For a COMPANY type user:
                    {
                        "type": "COMPANY",
                        "data": {
                            "companyName": "Example Corp",
                            "tradeName": "ExCorp",
                            "legalStructure": "LLC",
                            "description": "An example company",
                            "establishedOn": "2000-01-01",
                            "phone": "0987654321",
                            "address": {
                                "street1": "456 Market St",
                                "street2": "Suite 200",
                                "city": "San Francisco",
                                "state": "CA",
                                "zipCode": "94105",
                                "countryCode": "US"
                            },
                            "mainOwnerUser": "owner-user-id-456",
                            "ownerUsers": ["owner-user-id-456", "owner-user-id-789"],
                            "naics": "123456",
                            "naicsDescription": "Example NAICS Description",
                            "document": {
                                "type": "ID_CARD",
                                "number": "B7654321",
                                "issuedCountryCode": "US"
                            }
                        },
                        "externalId": "external-id-456"
                    }

            Returns
            -------
            UserCreateResponse
                The response from the API as a dictionary. The structure is as follows:

                {
                    "customerId": "68a2d71f-80d6-4b2a-a38d-bdeecf909190",
                    "type": "PERSON",
                    "data": {
                        "firstName": "John",
                        "lastName": "Lennon",
                        "dateOfBirth": "1997-01-01",
                        "email": "email@killb.com",
                        "phone": "+5517922222222",
                        "document": {
                            "type": "PASSPORT",
                            "number": "3333333",
                            "issuedCountryCode": "BR"
                        },
                        "address": {
                            "street1": "Street 1",
                            "zipCode": "11111",
                            "city": "City",
                            "countryCode": "BR",
                            "state": "SP"
                        }
                    },
                    "isBlocked": false,
                    "accessLevel": "L0",
                    "active": true,
                    "createdAt": "2024-06-10T14:08:17.484Z",
                    "updatedAt": "2024-06-10T14:08:17.484Z",
                    "id": "aac82890-9fca-4e91-940c-8836ec822b45"
                }
        """
        return self.api_requests.request(method="POST", endpoint="users", json=data)

    def update(self, data: Union[PersonData, CompanyData], user_id: str) -> UserCreateResponse:
        """
            Updates an existing user.

            Parameters:
            ----------
            data : dict
                The updated user data.
            user_id : str
                The ID of the user to update.

            Returns:
            -------
            dict
                The response from the API as a dictionary.
        """
        return self.api_requests.request(method="PATCH", endpoint=f"users/{user_id}", json=data)

    def get_by_query(self, data: GetUserByQuery):
        """
            Retrieves users based on query parameters.

            Parameters:
            ----------
            query_params : dict
                The query parameters.

            Returns:
            -------
            dict
                The response from the API as a dictionary.
        """
        query_string = urlencode(data)
        return self.api_requests.request(method="GET", endpoint=f"users?{query_string}")
