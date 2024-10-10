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
PAYNOCCHIO is more than a typical payment processing service. We provide a comprehensive solution, operating as a ledger infrastructure. Our integrated services include roles as an issuing processor and program manager, along with offering closed-loop wallets. This enhances our extensive capabilities in payment processing.

## Before you begin

- Register at Paynocchio control panel
- Create at least one environment and add at least one API key 

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

### Using example

```python
# Import paynocchio client
from paynocchio.client import Client

# Get client connection
client = Client(
    # API obtained at Paynocchio control panel
    api_key="6e229b0e-7a4d-4952-b8e9-c8fb2d33219d", 
    # UUID of your environment obtained at Paynocchio control panel
    env_id="a2860217-a6b2-4fb9-9a7b-32e217651e16",  
    # UUID generated on your side and related to user account 
    user_id=user 
)

# Get wallet by environment uuid
wallet = client.create_wallet(
    data={
        "environment_uuid":"a2860217-a6b2-4fb3-9a7b-32e123651e16",
        "user_id": "a2820337-a6b2-4fb9-9a1b-32q217651e55",
        "type_uuid": "93ac9017-4110-41bf-be2d-aa123884451d",
    }
)
```

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
[our site](https://paynocchio.com/team)
