from paynocchio.api_client import Api


class Client(Api):
    def __init__(self, api_key: str, environment_uuid: str, user_uuid: str, test_mode: str) -> None:
        self.base_uri = 'wallet.paynocchio.com'
        super(Client, self).__init__(api_key, environment_uuid, user_uuid, test_mode)
