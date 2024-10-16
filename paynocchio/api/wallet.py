# coding: utf-8

"""
    Paynocchio API

    The Paynocchio REST API. Please visit https://www.paynocchio.com

    Contact: developers@paynocchio.com
"""  # noqa: E501


def create_wallet(self, data: dict) -> dict:
    """
    Create wallet for specified user with specified type.

    data:
        environment_uuid: UUID Admin panel environment ID.
        user_uuid: UUID External system user id.

    headers:
        X-Wallet-Signature: sha256
        X-Test-Mode-Switch: on/off

    Response:
        uuid: UUID4
        user_uuid: UUID4
        status: StatusSchema(
            uuid: UUID
            updated_at: Datetime
            title: str
            code: str
        )
        balance: BalanceSchema(
            uuid: UUID
            updated_at: Datetime
            iso_currency_code: str
            current: int
        )
        number: int
        created_at: datetime
        rewarding_balance: int
        currency_uuid: UUID
    """
    return self.sign_request('wallet', 'POST', '/wallet', body_data=data)


def update_wallet_status(self, data: dict) -> dict:
    """
    Suspend, Activate or Block Wallet by UUID.
    Please take attention: Blocked wallets can't be activated.

    data:
        uuid: UUID Admin panel Wallet id.
        environment_uuid: UUID Admin panel Environment id
        user_uuid: UUID External system user id.
        status_uuid: UUID Wallet system status id.

    headers:
        X-Wallet-Signature: sha256
        X-Test-Mode-Switch: on/off

    Response:
        uuid: UUID4
        updated_at: Datetime
        user_uuid: UUID4
        type: TypeSchema(
            uuid: UUID
            updated_at: Datetime
            title: str
            description: str
        )
        status: StatusSchema(
            uuid: UUID
            updated_at: Datetime
            title: str
            code: str
        )
        balance: BalanceSchema(
            uuid: UUID
            updated_at: Datetime
            iso_currency_code: str
            current: int
        )
        number: int
        created_at: datetime
        rewarding_balance: int
        currency_uuid: UUID
    """
    return self.sign_request('wallet', 'PATCH', '/wallet', body_data=data)


def wallet_environment_structure(self, params: dict) -> dict:
    """
    To get Wallet Environment Structure with all current settings including rewarding groups with rules

    params:
        user_uuid: UUID External system user id.
        environment_uuid: UUID Admin panel Environment id

    headers:
        X-Wallet-Signature: sha256

    Response:
        uuid: UUID4
        title: str
        company_uuid: UUID4
        created_at: Datetime
        keys_number: int
        card_balance_limit: int
        daily_transaction_limit: int
        multiple_accounts_limit: int
        minimum_topup_amount: int
        bonus_conversion_rate: float
        allow_withdraw: bool
        rewarding_groups: RewardingGroupsSchema(
            title: str
            date_from: Datetime
            date_to: Datetime
            active: bool
            rewarding_rules: RewardingRulesSchema(
                title: str
                operation_type: str
                value: int
                value_type: str
                min_amount: int
                max_amount: int
                conversion_rate: float
            )
        )
    """
    return self.sign_request('wallet', 'GET', '/wallet/environment-structure', params=params)


def wallet_transaction_history(self, params: dict) -> dict:
    """
    To get paginated list of Wallet Transaction History

    params:
        user_uuid: UUID External system user id.
        environment_uuid: UUID Admin panel Environment id
        wallet_uuid: UUID Admin panel Environment id
        page: int = 1, start page
        size: int = 30, size of the paginator list
        start: datetime | None = None,
        end: datetime | None = None,

    headers:
        X-Wallet-Signature: sha256
        X-Test-Mode-Switch: on/off

    Response:
        item: PrimaryAccountingDocumentsLogSchema(
            uuid: UUID4 = uuid4()
            external_request_id: str = str(uuid4())
            created_at: datetime
            company_id: UUID4
            payment_method: str
            amount: int
            currency_id: Optional[UUID4] = None
            wallet_uuid: UUID4
            user_uuid: UUID4
            status: str
            )
        total: int
        page: int
        size: int
        pages: int
    """
    return self.sign_request('wallet', 'GET', '/wallet/environment-structure', params=params)


def calculate_commissions_and_bonuses(self, params: dict) -> dict:
    """
    To get calculation of Commission and Bonuses according to amount for different types of operations

    params:
        user_uuid: UUID External system user id.
        environment_uuid: UUID Admin panel Environment id
        wallet_uuid: UUID Admin panel Environment id
        amount: float amount of transaction
        operation_type: Optional[str] name of the operation
        wallet_balance_check: Optional[bool] enable/disable check of the user wallet balances,

    headers:
        X-Wallet-Signature: sha256
        X-Test-Mode-Switch: on/off

    Response:
        environment_uuid: UUID
        wallet_uuid: UUID
        conversion_rate: float
        operations_data: OperationSchema(
                type_operation: str,
                full_amount: float,
                bonuses_amount: int,
                commission_amount: float
            )
    """
    return self.sign_request('wallet', 'GET', '/wallet/environment-structure', params=params)


def get_wallets(self, environment_uuid: str,  params: dict) -> dict:
    """
    To get list of wallets in Environment

    params:
        environment_uuid: UUID Environment.

    headers:
        X-Wallet-Signature: sha256
        X-Test-Mode-Switch: on/off
    
    Response:
        item: list[
            uuid: UUID4
            user_uuid: UUID4
            status: StatusSchema(
                uuid: UUID
                updated_at: Datetime
                title: str
                code: str
            )
            balance: BalanceSchema(
                uuid: UUID
                updated_at: Datetime
                iso_currency_code: str
                current: int
            )
            number: int
            created_at: datetime
            updated_at: datetime|null
            rewarding_balance: int
            currency_uuid: UUID4
        ]
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{environment_uuid}/get_list', params=params)


def get_wallets_by_user_uuid(self, environment_uuid: str, user_uuid: str,  params: dict) -> dict:
    """
    To get list of wallets in Environment.

    params:
        user_uuid: UUID External system user id.
        environment_uuid: UUID External system user id.

    headers:
        X-Wallet-Signature: sha256
        X-Test-Mode-Switch: on/off

    Response:
        item: list[
            uuid: UUID4
            user_uuid: UUID4
            status: StatusSchema(
                uuid: UUID
                updated_at: Datetime
                title: str
                code: str
            )
            balance: BalanceSchema(
                uuid: UUID
                updated_at: Datetime
                iso_currency_code: str
                current: int
            )
            number: int
            created_at: datetime
            updated_at: datetime|null
            rewarding_balance: int
            currency_uuid: UUID4
        ]
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{environment_uuid}/get_wallet_from_uuid/{user_uuid}', params=params)


def get_wallet(self, wallet_id: str, params: dict) -> dict:
    """
    To get wallet by id with balance.

    params:
        environment_uuid: UUID Admin panel environment ID
        user_uuid: UUID External system user id

    headers:
        X-Wallet-Signature: sha250
        X-Test-Mode-Switch: on/off
    
    Response:
        uuid: UUID4
        user_uuid: UUID4
        status: StatusSchema(
            uuid: UUID
            updated_at: Datetime
            title: str
            code: str
        )
        balance: BalanceSchema(
            uuid: UUID
            updated_at: Datetime
            iso_currency_code: str
            current: int
        )
        number: int
        created_at: datetime
        updated_at: datetime|null
        rewarding_balance: int
        currency_uuid: UUID4
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{wallet_id}', params=params)
