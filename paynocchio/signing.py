import requests
import json

from paynocchio.check_response import exception_catch


def sign_request(
        self,
        api: str,
        method: str,
        endpoint: str,
        params: dict = None,
        body_data: dict = None,
        test_mode: str = "off"
) -> dict:
    url = f'https://{self.base_uri}{endpoint}'
    response = requests.request(
        method=method,
        url=url,
        headers={
            "X-Wallet-Signature": self.api_key,
            "X-Test-Mode-Switch": test_mode
            },
        data=json.dumps(body_data),
        params=params
    )
    exception_catch(api, response)
    return json.loads(response.text)