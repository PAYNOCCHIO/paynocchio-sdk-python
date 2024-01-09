from abc import ABC
from paynocchio.generate_api_key import calculate_sha256


class Api(ABC):
    def __init__(self, api_key: str, env_id: str, user_id: str) -> None:
        self.api_key = calculate_sha256(api_key, env_id, user_id)

    from paynocchio.api.wallet import create_wallet

    from paynocchio.signing import sign_request
