# Kill-B Python SDK

## This is the official Python SDK for interacting with the Kill-B API V2.

--------

## Installation

You can install the SDK via pip:

```bash
  pip install killb-sdk-python
```

### Requirements

This SDK requires only the requests library. You can install it using pip:

```bash
  pip install requests
```

## Usage

### Authentication

To start using the SDK, you need to authenticate with your Kill-B API credentials:

```python
from killb.client import Client

# ENVIRONMENT -> available environment is SANDBOX and PRODUCTION - please test first to go to PRODUCTION

# Replace with your environment, email, password, and API key
client = Client(environment="SANDBOX", email="your@email.com", password="your_password",
                api_key="your_api_key")
```

### Creating a User

You can create a user using the User class:

```python
    user_data = {
            "type": "PERSON",
            "data": {
                "firstName": "Bruce",
                "lastName": "Wayne",
                "dateOfBirth": "1982-01-28",
                "email": "wayne@batman.com",
                "phone": "+5511933222111",
                "document": {
                    "type": "PASSPORT",
                    "number": "BAT0001",
                    "issuedCountryCode": "US"
                },
                "address": {
                    "street1": "Street1",
                    "zipCode": "00315",
                    "city": "Gotham",
                    "countryCode": "US",
                    "state": "GO"
                }
            }
    }

    user_client = client.User.create(user_data)
    print("User created successfully:", user_client)
```


### Creating Account

You can create account using the Account class:

````python
    account_data = {
	"type": "SPEI",
	"userId": user["id"],
	"data": {
		"firstName": "Selina",
		"lastName": "Kyle",
        "phone": "+5511933222111",
        "email": "selina@cat.com",
        "bankCode": "1211",
        "countryCode": "MX",
        "clabe": "ASDFASDFASDFA",
		"document": {
            "type": "PASSPORT",
			"number": "CAT221122",
			"issuedCountryCode": "US"
		    }
	    }
    }

    account = client.Account.create(account_data)
    print("Account created successfully:", account)
````

------

For more detailed documentation and examples, please refer to the [API documentation](https://killbapi.stoplight.io/docs/killb-v2/365bbddbae725-api-version-2-0-new-features-overview).
