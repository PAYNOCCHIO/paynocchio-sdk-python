from abc import ABC
from paynocchio.generate_api_key import calculate_sha256


class Api(ABC):
    def __init__(self, api_key: str, environment_uuid: str, user_uuid: str, test_mode: str = "off") -> None:
        self.api_key = calculate_sha256(api_key, environment_uuid, user_uuid)
        self.test_mode = test_mode

    from paynocchio.api.wallet import (create_wallet, update_wallet_status, wallet_environment_structure,
                                       wallet_transaction_history, calculate_commissions_and_bonuses, get_wallets,
                                       get_wallets_by_user_uuid, get_wallet,
                                       )
    from paynocchio.api.order import get_order, get_orders_by_wallet_uuid
    from paynocchio.api.operation import  topup_wallet, payment_wallet, withdraw_wallet
    from paynocchio.api.health import get_health, check_signature
    from paynocchio.api.status import get_status

    from paynocchio.signing import sign_request
