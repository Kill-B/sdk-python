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
from killb_sdk_python import Client

# Replace with your environment, email, password, and optional API key
api_client = Client(environment='production', email='your@email.com', password='your_password', api_key='your_api_key')
```

### Creating a User

You can create a user using the User class:

```python
# Create user data
user_data = {
    'firstName': 'John',
    'lastName': 'Doe',
    'dateOfBirth': '1990-01-01',
    'email': 'john@example.com',
    # Add other required fields
}

# Create the user
user_client = api_client.User.create(user_data)
print("User created successfully:", user_client)
```

For more detailed documentation and examples, please refer to the [API documentation](https://killbapi.stoplight.io/docs/killb-v2/365bbddbae725-api-version-2-0-new-features-overview).
