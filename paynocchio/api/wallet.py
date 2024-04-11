def create_wallet(self, data: dict) -> dict:
    """
    Create wallet for specified user with specified currency and type.

    data:
        env_id: UUID Admin panel environment ID.
        user_id: UUID External system user id.
    
    Response:
        uuid: UUID4
        user_uuid: UUID4
        currency: CurrencySchema(
            alphabetic_code: str
            numeric_code: str
            minor_unit: str
        )
        balance: BalanceSchema(
            iso_currency_code: str
            current: int
        )
        number: int
        created_at: datetime
        rewarding_balance: int
    """
    return self.sign_request('wallet', 'POST', '/wallet', body_data=data)


def get_wallets(self, params: dict) -> dict:
    """
    To get list of wallets of the authorized user.

    params:
        env_id: UUID Admin panel environment ID.
        user_id: UUID External system user id.
    
    Response:
        wallets: list[
            uuid: UUID4
            user_uuid: UUID4
            currency: CurrencySchema(
                alphabetic_code: str
                numeric_code: str
                minor_unit: str
            )
            balance: BalanceSchema(
                iso_currency_code: str
                current: int
            )
            number: int
            created_at: datetime
            rewarding_balance: int
        ]
    """
    return self.sign_request('wallet', 'GET', '/wallet', params=params)


def get_wallet(self, wallet_id: str, params: dict) -> dict:
    """
    To get wallet by id with balance.

    params:
        env_id: UUID Admin panel environment ID
        user_id: UUID External system user id
    
    Response:
        uuid: UUID4
        user_uuid: UUID4
        currency: CurrencySchema(
            alphabetic_code: str
            numeric_code: str
            minor_unit: str
        )
        balance: BalanceSchema(
            iso_currency_code: str
            current: int
        )
        number: int
        created_at: datetime
        rewarding_balance: int
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{wallet_id}', params=params)


def withdraw_wallet(self, data: dict) -> dict:
    """
    To withdraw money from the wallet back to the user’s bank card.

    data:
        user_uuid: Optional[UUID4]
        type_operation: Optional[str]
        request_uuid: Optional[UUID4]
        status_type: str
        currency: str
        amount: int | float
        wallet_uuid: Optional[UUID4]
        company_id: Optional[UUID4]
        environment_uuid: UUID4
    """
    return self.sign_request('wallet', 'POST', '/wallet/withdraw', body_data=data)


def topup_wallet(self, data: dict) -> dict:
    """
    To top up wallet with desired sum by bank card.

    data:
        user_uuid: Optional[UUID4]
        type_operation: str
        amount: int | float
        currency: str
        wallet_uuid: Optional[UUID4]
        company_id: Optional[UUID4]
        environment_uuid: UUID4
    """
    return self.sign_request('wallet', 'POST', '/wallet/topup', body_data=data)


def payment_wallet(self, data: dict) -> dict:
    """
    To allow users to initiate a payment for customer services.

    data:
        user_uuid: Optional[UUID4]
        type_operation: str
        company_id: Optional[UUID4]
        currency: str
        wallet_uuid: Optional[UUID4]
        external_order_id: Optional[UUID4]
        amount: int | float
        full_amount: int | float
        bonus_amount: Optional[int | float]
        environment_uuid: UUID4
    """
    return self.sign_request('wallet', 'POST', '/wallet/payment', body_data=data)
