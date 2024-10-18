<p align="center">
<img style="align:center;" src="resources/logo.png" alt="Paynocchio Logo" width="100"/>
<h1 align="center">Paynocchio Python SDK</h1>
</p>

**[Quickstart](#Quickstart)** |
**[Documentation](https://github.com/PAYNOCCHIO/paynocchio-api-alpha/tree/doc/readme-feature/API)** |
**[Site](https://paynocchio.com/)** |
**[License](#License)** |
**[Team](#Team)** |

## Overview
[PAYNOCCHIO](https://paynocchio.com) is more than a typical payment processing service. We provide a comprehensive solution, operating as a ledger infrastructure. Our integrated services include roles as an issuing processor and program manager, along with offering closed-loop wallets. This enhances our extensive capabilities in payment processing.

## Before you begin

- Register at [Paynocchio control panel](https://paynocchio.com)
- Create at least one wallet group and add at least one API key 

## Quickstart

### Create virtualenv
```
virtualenv venv
```

### Activate virtualenv

**linux or Mac**
```
source venv/bin/activate
```
**Windows**
```
.\venv\Scripts\activate
```

### Install paynocchio library
```
pip install paynocchio
pip3 install paynocchio
```

# Paynocchio Client Example

This example demonstrates how to integrate and use the Paynocchio API to create a wallet for a specific user in a controlled wallet group.

### Steps:

1. **Import the Paynocchio Client**:  
   The first step is importing the `Client` class from the `paynocchio` library and the `uuid4` function from the `uuid` module for user identification.

2. **Generate a User UUID**:  
   A UUID is generated on your side to uniquely identify the user in Paynocchio.

3. **Establish a Client Connection**:  
   To interact with the Paynocchio API, create an instance of the `Client` class. You'll need:
   - `api_key`: The API key obtained from the Paynocchio control panel.
   - `environment_uuid`: The environment UUID, also from the control panel, representing your operating wallet group.
   - `user_uuiid`: A unique identifier for the user (UUID format), generated on your system.
   - `test_mode`: Set to `true` to enable testing without affecting live data.

4. **Create a Wallet for the User**:  
   Using the `create_wallet` method, a wallet is created for the user within a specific wallet group. You'll pass a dictionary containing the environment UUID and user UUID as part of the request.

## Establish a Client Connection

```python
# Import paynocchio client
from paynocchio.client import Client
from uuid import uuid4

# Generate user UUID
user = str(uuid4())

# Get client connection
client = Client(
    # API obtained at Paynocchio control panel
    api_key="6e229b0e-7a4d-4952-b8e9-c8fb2d33219d", 
    # UUID of your wallet group obtained at Paynocchio control panel
    environment_uuid="a2860217-a6b2-4fb9-9a7b-32e217651e16",  
    # UUID generated on your side and related to user account 
    user_uuid=user,
    # Enable test mode
    test_mode="on"
)

```

## Create Wallet

 Create wallet for specified user with specified wallet group

#### Example Code

```python
# Create wallet by wallet group UUID and user UUID
wallet = client.create_wallet(
    data={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
    }
)

```

**Request Parameters**
- **environment_uuid** (string, required):
The UUID representing the wallet group where the reward group is configured. This parameter defines the context for the commissions and bonuses.

- **user_uuid** (string, required):
The UUID of the user for whom the calculation is being made. This identifies the external user tied to the transaction.

## Get Available Wallet Statuses

This example demonstrates how to retrieve the available statuses for wallets using the Paynocchio API. 

The `get_status` method is part of the `Client` class and allows you to fetch the current wallet statuses defined in the system.

#### Example Code

```python
# Fetch available wallet statuses
statuses = client.get_status()

```

## Update Wallet Status

This example demonstrates how to update the status of a specific wallet using the Paynocchio API. The `update_wallet_status` method allows you to change the status of a wallet based on its unique identifier.

#### Example Code

```python
# Update the status of a specific wallet
response = client.update_wallet_status(
    data={
        "uuid": "5eea41d8-e459-4f41-91cd-763fe7708f8e",
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "status_uuid": "2e50118d-cf3c-47e2-a73c-1826adc32768"
    }
)

```
**Request Parameters**

...

- **uuid** (string, required):
The UUID of the wallet that belongs to the user. This parameter is mandatory, but in cases where no wallet exists (such as for anonymous users), the wallet_balance_check parameter can be set to false.

- **status_uuid** (string, required):
The UUID of the actual wallet status obtained with `client.get_status()` function


## Get Wallet Group Structure

This example demonstrates how to retrieve the structure and status of wallets within a specific wallet group using the Paynocchio API. The `wallet_environment_structure` method provides details about wallet groups and their statuses for a particular user in a specified environment.

#### Example Code

```python
# Fetch the wallet environment structure and status
response = client.wallet_environment_structure(
    params={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
    }
)
```

## Get Wallet Transaction History

This example demonstrates how to retrieve the transaction history of a specific wallet using the Paynocchio API. The `wallet_transaction_history` method provides details about transactions associated with a wallet for a particular user in a specified environment.

#### Example Code

```python
# Fetch the transaction history for a specific wallet
response = client.wallet_transaction_history(
    params={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "wallet_uuid": "5eea41d8-e459-4f41-91cd-763fe7708f8e",
        "page": 1,
        "size": 10
    }
)

```

## Calculate commissions and bonuses
This API method calculates the commissions and bonuses based on a provided transaction amount and the active reward group within a given environment. The calculation can be performed for different types of operations, and it supports scenarios where no wallet exists, such as for anonymous users.

```python

response = client.calculate_commissions_and_bonuses(
    params={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "wallet_uuid": "5eea41d8-e459-4f41-91cd-763fe7708f8e",
        "amount": 100,
        "operation_type": "operation_type",
        "wallet_balance_check": "false"
    }
)

```

**Request Parameters**

...
- **amount** (float, required):
The transaction amount used to calculate the commission and bonus. This is the core value for the calculation.

- **operation_type** (string, optional):
Specifies the exact operation type (e.g., `payment_operation_add_money` and `payment_operation_for_services`) for which the calculation is being made. If not provided, the default operation will be used.

- **wallet_balance_check** (boolean, optional):
Indicates whether to check the balance of the wallet when performing the calculation. Set this to false when there is no wallet available (e.g., for anonymous users).


## Get the list of the wallets within a Wallet Group
This API method retrieves a list of wallets associated with a specified environment. It allows you to paginate the results to manage large sets of data effectively.
```python

response = client.get_wallets(
    environment_uuid="a2860217-a6b2-4fb3-9a7b-32e123651e16",
    params={
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "page": 1,
        "size": 10,
    }
)

```

## Get Wallet balance
This API method retrieves the current balance of a specified wallet. It allows users to check the amount of funds available in their wallet within a given environment.

```python

response = client.get_wallet(
    wallet_uuid="5eea41d8-e459-4f41-91cd-763fe7708f8e",
    params={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
    }
)

```

# Orders
## Get Order by UUID
The `get_order` method retrieves detailed information about a specific order by its UUID. This method is part of a service that communicates with an external system to manage orders, including signature validation and test mode switching via headers.

```python

response = client.get_order(
    order_uuid="5eea41d8-e459-4f41-91cd-763fe7708f8e",
    params={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
    }
)

```

**Request Parameters**

...
- order_uuid (str):
The unique identifier (UUID) of the order that needs to be fetched.


## Get All Orders by Wallet UUID

This section describes how to retrieve all orders associated with a specific wallet UUID using the `get_orders_by_wallet_uuid` method from the client.

```python

response = client.get_orders_by_wallet_uuid(
    params={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "wallet_uuid": "5eea41d8-e459-4f41-91cd-763fe7708f8e"
    }
)

```

# Operations

## Top Up Wallet

This API method allows users to top up their wallet by a specified amount using a bank card. The process requires the environment, user, and wallet details, as well as the amount to be credited and a redirect URL for the post-payment flow.

---

#### Example Usage
```python
response = client.topup_wallet(
    data={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "wallet_uuid": "5eea41d8-e459-4f41-91cd-763fe7708f8e",
        "amount": 100.34,
        "redirect_url": "https://your-super-app.site"
    }
)
```
**Request Parameters**

...
- **amount** (float, required): The amount of money to add to the wallet. Example: 100.34.
- **redirect_url** (string, required): The URL to redirect the user to after the top-up process. Example: "https://your-super-app.site".


## Payment from Wallet

This API method initiates a payment from a user's wallet for customer services. It requires the environment, user, wallet details, and payment amount, along with an external order ID and other relevant payment details.

#### Example Usage
```python
response = client.payment_wallet(
    data={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "wallet_uuid": "5eea41d8-e459-4f41-91cd-763fe7708f8e",
        "external_order_id": "606589a2-190a-4b5e-ac9a-aef7d989dbbc",
        "amount": 100.34,
        "full_amount": 100.34,
        "bonus_amount": 0
    }
)
```
**Request Parameters**

...
* **external_order_id** (UUID, required): A unique identifier for the external order related to the payment.
* **amount** (float, required): The primary amount to be charged from the wallet.
* **full_amount** (float, required): The total amount for the transaction, including bonuses or adjustments.
* **bonus_amount** (float, optional): Any additional bonus amount applied to the transaction.


## Withdrawal from Wallet

This API method allows users to initiate a withdrawal from their wallet. It requires the user’s unique identifiers, the amount to withdraw, and the currency for the transaction.

---

#### Example Usage
```python
response = client.withdraw_wallet(
    data={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_uuid": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "wallet_uuid": "5eea41d8-e459-4f41-91cd-763fe7708f8e", 
        "currency": "USD",  
        "amount": 20  
    }
)
```
**Request Parameters**

...
* **currency** (string, required): The ISO 4217 3-letter code for the currency of the transaction (e.g., "USD").
* **amount** (float, required): The amount of money to withdraw from the wallet. This must be a positive value.

# Health

## Check if Service is working

This API method checks if the database connection is healthy and returns a status indicating whether the service is operational.

---

#### Example Usage
```python
response = client.get_health()
```

## Check if API key and Environment UUID are valid

This API method verifies the validity of the provided API key and Environment UUID. It's used to ensure that the integration is properly configured with a valid environment and API credentials.

---

#### Example Usage
```python
response = client.check_signature(
    data={
        "environment_uuid": "a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "secret_key": "f2c24b92-d7e2-49f6-a111-12b44c564c63"
    }
)
```

**Request Parameters**

...
- **secret_key** (UUID): The API key obtained in Development section of the Paynocchio Control panel.


## Team

- __Abay Serkebayev__        | CEO / Founder
- __Mikhail Moiseev__        | System Analyst
- __Anastasia Maximova__     | Business Analyst
- __Alexander Mochinov__     | BackEnd Engineer
- __Semyon Berezovsky__      | BackEnd Engineer
- __Ivan Tsenilov__          | FrontEnd Engineer
- __Sergey Anishchenko__     | FrontEnd Engineer
- __Ilya Poplavsky__         | QA Engineer
- __Anton Abramenko__        | DevOps Engineer

## Changelog
See [CHANGELOG.md](https://github.com/PAYNOCCHIO/paynocchio-api-alpha/blob/main/CHANGELOG.md) for details.

## License
MIT [license](https://github.com/PAYNOCCHIO/paynocchio-api-alpha/blob/main/LICENSE)

## Stay in touch
[our site](https://paynocchio.com/)
