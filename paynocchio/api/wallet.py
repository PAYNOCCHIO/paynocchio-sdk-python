def create_wallet(self, data: dict) -> dict:
    """
    Create wallet for specified user with specified currency and type.

    data:
        env_id: UUID Admin panel environment ID.
        user_id: UUID External system user id.
    
    Response:
        wallet_id: UUID
    """
    return self.sign_request('wallet', 'POST', '/wallet', body_data=data)


def get_wallets(self, params: dict) -> dict:
    """
    To get list of wallets of the authorized user.

    params:
        env_id: UUID Admin panel environment ID.
        user_id: UUID External system user id.
    
    Response:
        wallets: list
        wallet.id: UUID
        wallet.user_id: UUID
        wallet.balance: double
        wallet.currency: str
        wallet.status: str
    """
    return self.sign_request('wallet', 'GET', '/wallet', params=params)


def get_wallet(self, wallet_id: str, params: dict) -> dict:
    """
    To get wallet by id with balance.

    params:
        env_id: UUID Admin panel environment ID
        user_id: UUID External system user id
    
    Response:
        env_id: UUID
        user_id: UUID
        balance: double
        currency: str
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{wallet_id}', params=params)


def change_wallet_status(self, wallet_id: str, params: dict) -> dict:
    """
    To change wallet status.

    params:
        env_id: UUID Admin panel environment ID
        user_id: UUID External system user id
    
    Response:
        env_id: UUID
        user_id: UUID
        balance: double
        currency: UUID
        status: str
    """
    return self.sign_request('wallet', 'PATCH', f'/wallet/{wallet_id}/status', params=params)


def withdraw_wallet(self, data: dict) -> dict:
    """
    To withdraw money from the wallet back to the user’s bank card.

    data:
        env_id: UUID Admin panel environment ID.
        user_id: UUID External system user id.
        wallet_id: UUID.
        amount: float.
    """
    return self.sign_request('wallet', 'POST', '/wallet/withdraw', body_data=data)


def topup_wallet(self, data: dict) -> dict:
    """
    To top up wallet with desired sum by bank card.

    data:
        env_id: UUID Admin panel environment ID.
        user_id: UUID External system user id.
        wallet_id: UUID.
        amount: float.
    """
    return self.sign_request('wallet', 'POST', '/wallet/topup', body_data=data)


def payment_wallet(self, data: dict) -> dict:
    """
    To allow users to initiate a payment for customer services.

    data:
        env_id: UUID Admin panel environment ID.
        user_id: UUID External system user id.
        wallet_id: UUID.
        amount: float.
        product_id: UUID External system product or service ID.
    """
    return self.sign_request('wallet', 'POST', '/wallet/payment', body_data=data)
