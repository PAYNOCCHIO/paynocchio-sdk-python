from paynocchio.api_client import Api


class Client(Api):
    def __init__(self, api_key: str, env_id: str, user_id: str) -> None:
        self.base_uri = 'wallet.dev.paynocchio.com'
        super(Client, self).__init__(api_key, env_id, user_id)
