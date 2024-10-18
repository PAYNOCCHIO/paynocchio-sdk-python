# coding: utf-8

"""
    Paynocchio API

    The Paynocchio REST API. Please visit https://www.paynocchio.com

    Contact: developers@paynocchio.com
"""  # noqa: E501


def create_wallet(self, data: dict) -> dict:
    """
    Creates a wallet for a specified user with a given type.

    This method allows for the creation of a wallet, linking it to a user in the external system
    while specifying the wallet group in which the wallet will operate.

    Args:
        data (dict): A dictionary containing the following required parameters:
            environment_uuid (str): The UUID of the admin panel wallet group (required).
            user_uuid (str): The UUID of the user from the external system (required).

    Returns:
        dict: A dictionary containing the details of the created wallet with the following fields:
            uuid (str): The unique identifier for the newly created wallet (UUID4).
            user_uuid (str): The UUID of the user associated with the wallet (UUID4).
            status (dict): A dictionary representing the status of the wallet, containing:
                uuid (str): The unique identifier for the status (UUID).
                updated_at (str, ISO 8601 format): The date and time when the status was last updated.
                title (str): A human-readable title describing the status.
                code (str): A machine-readable code representing the status.
            balance (dict): A dictionary representing the wallet's balance, containing:
                uuid (str): The unique identifier for the balance (UUID).
                updated_at (str, ISO 8601 format): The date and time when the balance was last updated.
                iso_currency_code (str): The ISO currency code (e.g., "USD").
                current (int): The current balance amount.
            number (int): The wallet number.
            created_at (str, ISO 8601 format): The date and time when the wallet was created.
            rewarding_balance (int): The rewarding balance associated with the wallet.
            currency_uuid (str): The unique identifier for the currency used in the wallet (UUID).

    Notes:
        Ensure that the UUIDs provided are valid and correspond to existing records.
        The wallet will be created in the specified wallet group and linked to the specified user.
    """
    return self.sign_request('wallet', 'POST', '/wallet', body_data=data)


def update_wallet_status(self, data: dict) -> dict:
    """
    Updates the status of a wallet identified by its UUID.

    This method allows you to suspend, activate, or block a wallet.
    Note that once a wallet is blocked, it cannot be activated again.

    Args:
        data (dict): A dictionary containing the following required parameters:
            uuid (str): The UUID of the wallet to be updated (Admin panel Wallet ID).
            environment_uuid (str): The UUID of the admin panel wallet group (required).
            user_uuid (str): The UUID of the user from the external system (required).
            status_uuid (str): The UUID of the new status to be assigned to the wallet (required).

    Returns:
        dict: A dictionary containing the updated details of the wallet with the following fields:
            uuid (str): The unique identifier for the wallet (UUID4).
            updated_at (str, ISO 8601 format): The date and time when the wallet status was last updated.
            user_uuid (str): The UUID of the user associated with the wallet (UUID4).
            type (dict): A dictionary representing the type of the wallet, containing:
                uuid (str): The unique identifier for the wallet type (UUID).
                updated_at (str, ISO 8601 format): The date and time when the wallet type was last updated.
                title (str): A human-readable title describing the wallet type.
                description (str): A detailed description of the wallet type.
            status (dict): A dictionary representing the current status of the wallet, containing:
                uuid (str): The unique identifier for the status (UUID).
                updated_at (str, ISO 8601 format): The date and time when the status was last updated.
                title (str): A human-readable title describing the status.
                code (str): A machine-readable code representing the status.
            balance (dict): A dictionary representing the wallet's balance, containing:
                uuid (str): The unique identifier for the balance (UUID).
                updated_at (str, ISO 8601 format): The date and time when the balance was last updated.
                iso_currency_code (str): The ISO currency code (e.g., "USD").
                current (int): The current balance amount.
            number (int): The wallet number.
            created_at (str, ISO 8601 format): The date and time when the wallet was created.
            rewarding_balance (int): The rewarding balance associated with the wallet.
            currency_uuid (str): The unique identifier for the currency used in the wallet (UUID).
    """
    return self.sign_request('wallet', 'PATCH', '/wallet', body_data=data)


def wallet_environment_structure(self, params: dict) -> dict:
    """
    Retrieves the current structure of the wallet group, including settings and rewarding groups with rules.

    This method provides detailed information about the wallet group, such as company UUID, created date,
    transaction limits, and rules for rewarding groups.

    Args:
        params (dict): A dictionary containing the following required parameters:
            user_uuid (str): The UUID of the user in the external system (required).
            environment_uuid (str): The UUID of the admin panel wallet group (required).

    Returns:
        dict: A dictionary containing the wallet group structure with the following fields:
            uuid (str): The unique identifier for the wallet group (UUID4).
            title (str): The title or name of the wallet group.
            company_uuid (str): The unique identifier for the company associated with this wallet group (UUID4).
            created_at (str, ISO 8601 format): The date and time when the wallet group was created.
            keys_number (int): The number of keys associated with the wallet.
            card_balance_limit (int): The limit on the card balance.
            daily_transaction_limit (int): The limit on daily transactions.
            multiple_accounts_limit (int): The limit on multiple accounts that can be created.
            minimum_topup_amount (int): The minimum amount that can be topped up.
            bonus_conversion_rate (float): The conversion rate for bonuses.
            allow_withdraw (bool): Indicates whether withdrawals are permitted.
            rewarding_groups (list): A list of rewarding groups associated with this wallet group, containing:
                title (str): The title of the rewarding group.
                date_from (str, ISO 8601 format): The start date of the rewarding group.
                date_to (str, ISO 8601 format): The end date of the rewarding group.
                active (bool): Indicates whether the rewarding group is currently active.
                rewarding_rules (list): A list of rules associated with the rewarding group, containing:
                    title (str): The title of the rewarding rule.
                    operation_type (str): The type of operation to which this rule applies.
                    value (int): The value associated with the rule.
                    value_type (str): The type of value (e.g., "fixed", "percentage").
                    min_amount (int): The minimum amount applicable under this rule.
                    max_amount (int): The maximum amount applicable under this rule.
                    conversion_rate (float): The conversion rate for the rewarding rule.
    """
    return self.sign_request('wallet', 'GET', '/wallet/environment-structure', params=params)


def wallet_transaction_history(self, params: dict) -> dict:
    """
    Retrieves a paginated list of the wallet's transaction history.

    This method allows users to fetch their wallet transaction records, with pagination support to navigate through multiple pages of results.

    Args:
        params (dict): A dictionary containing the following required parameters:
            user_uuid (str): The UUID of the user in the external system (required).
            environment_uuid (str): The UUID of the admin panel environment (required).
            wallet_uuid (str): The UUID of the specific wallet (required).
            page (int, optional): The page number to retrieve (default is 1).
            size (int, optional): The number of records per page (default is 30).
            start (datetime, optional): The start date for filtering transactions (default is None).
            end (datetime, optional): The end date for filtering transactions (default is None).

    Returns:
        dict: A dictionary containing the transaction history with the following fields:
            item (list): A list of transaction records, where each record contains:
                uuid (str): The unique identifier for the transaction (UUID4).
                external_request_id (str): The external request identifier (UUID4).
                created_at (str, ISO 8601 format): The date and time when the transaction was created.
                company_id (str): The unique identifier for the company associated with the transaction (UUID4).
                payment_method (str): The payment method used for the transaction (e.g., "credit_card", "bank_transfer").
                amount (int): The amount involved in the transaction (in the smallest currency unit, e.g., cents).
                currency_id (str, optional): The unique identifier for the currency (UUID4).
                wallet_uuid (str): The UUID of the wallet related to the transaction (UUID4).
                user_uuid (str): The UUID of the user who performed the transaction (UUID4).
                status (str): The current status of the transaction (e.g., "completed", "pending").
            total (int): The total number of transactions matching the query.
            page (int): The current page number of the results.
            size (int): The number of records returned per page.
            pages (int): The total number of pages available.
    """
    return self.sign_request('wallet', 'GET', '/wallet/transaction-history', params=params)



def calculate_commissions_and_bonuses(self, params: dict) -> dict:
    """
    Calculates commissions and bonuses based on the specified transaction amount for various operation types.

    This method retrieves the commission and bonus calculations for a given transaction amount, considering different types of operations.

    Args:
        params (dict): A dictionary containing the following parameters:
            user_uuid (str): The UUID of the user in the external system (required).
            environment_uuid (str): The UUID of the admin panel environment (required).
            wallet_uuid (str): The UUID of the wallet (required).
            amount (float): The amount of the transaction (required).
            operation_type (str, optional): The name of the operation for which commissions and bonuses are calculated.
            wallet_balance_check (bool, optional): A flag to enable or disable the check of the user's wallet balances (default is False).

    Returns:
        dict: A dictionary containing the commission and bonus calculations with the following fields:
            environment_uuid (str): The UUID of the environment in which the operation is performed.
            wallet_uuid (str): The UUID of the wallet related to the operation.
            conversion_rate (float): The conversion rate applicable to the transaction.
            operations_data (list): A list of operation details, where each entry contains:
                type_operation (str): The type of operation (e.g., "payment_operation_add_money", "payment_operation_for_services").
                full_amount (float): The total amount involved in the operation.
                bonuses_amount (int): The amount of bonuses earned from the operation.
                commission_amount (float): The commission charged for the operation.
    """
    return self.sign_request('wallet', 'GET', '/wallet/commissions-and-bonuses', params=params)



def get_wallets(self, environment_uuid: str, params: dict) -> dict:
    """
    Retrieves a list of wallets associated with a specific environment.

    This method fetches all wallets within the given environment, providing relevant details such as status, balance, and creation date.

    Args:
        environment_uuid (str): The UUID of the environment for which to retrieve the wallet list (required).

        params (dict): A dictionary containing optional query parameters for the request. Possible keys include:
            user_uuid (str, optional): The UUID of a specific user to filter the wallets.
            status_code (str, optional): The status code to filter wallets based on their current status.
            size (int, optional): The maximum number of wallets to return in the response.
            page (int, optional): The page number for pagination (default is 1).

    Returns:
        dict: A dictionary containing the following fields:
            item (list): A list of wallet details, where each wallet is represented as a dictionary with the following structure:
                uuid (str): The UUID of the wallet.
                user_uuid (str): The UUID of the user associated with the wallet.
                status (dict): A dictionary representing the status of the wallet, containing:
                    uuid (str): The UUID of the status.
                    updated_at (datetime): The timestamp when the status was last updated.
                    title (str): A human-readable title for the status.
                    code (str): A code representing the status.
                balance (dict): A dictionary representing the wallet balance, containing:
                    uuid (str): The UUID of the balance record.
                    updated_at (datetime): The timestamp when the balance was last updated.
                    iso_currency_code (str): The ISO 4217 currency code for the wallet's currency.
                    current (int): The current balance amount in the specified currency.
                number (int): The wallet number or identifier.
                created_at (datetime): The timestamp when the wallet was created.
                updated_at (datetime | None): The timestamp when the wallet was last updated, or None if not applicable.
                rewarding_balance (int): The rewarding balance amount associated with the wallet.
                currency_uuid (str): The UUID of the currency used for the wallet.
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{environment_uuid}/get_list', params=params)



def get_wallets_by_user_uuid(self, environment_uuid: str, user_uuid: str, params: dict) -> dict:
    """
    Retrieves a list of wallets associated with a specific user in a given environment.

    This method fetches all wallets that belong to the specified user within the provided environment. 

    Args:
        environment_uuid (str): The UUID of the environment from which to retrieve the wallets (required).
        user_uuid (str): The UUID of the user whose wallets are being retrieved (required).
        params (dict): A dictionary containing optional query parameters for the request. Possible keys include:
            size (int, optional): The maximum number of wallets to return in the response.
            page (int, optional): The page number for pagination (default is 1).
            status_code (str, optional): The status code to filter wallets based on their current status.

    Returns:
        dict: A dictionary containing the following fields:
            item (list): A list of wallet details, where each wallet is represented as a dictionary with the following structure:
                uuid (str): The UUID of the wallet.
                user_uuid (str): The UUID of the user associated with the wallet.
                status (dict): A dictionary representing the status of the wallet, containing:
                    uuid (str): The UUID of the status.
                    updated_at (datetime): The timestamp when the status was last updated.
                    title (str): A human-readable title for the status.
                    code (str): A code representing the status.
                balance (dict): A dictionary representing the wallet balance, containing:
                    uuid (str): The UUID of the balance record.
                    updated_at (datetime): The timestamp when the balance was last updated.
                    iso_currency_code (str): The ISO 4217 currency code for the wallet's currency.
                    current (int): The current balance amount in the specified currency.
                number (int): The wallet number or identifier.
                created_at (datetime): The timestamp when the wallet was created.
                updated_at (datetime | None): The timestamp when the wallet was last updated, or None if not applicable.
                rewarding_balance (int): The rewarding balance amount associated with the wallet.
                currency_uuid (str): The UUID of the currency used for the wallet.
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{environment_uuid}/get_wallet_from_uuid/{user_uuid}', params=params)


def get_wallet(self, wallet_id: str, params: dict) -> dict:
    """
    Retrieves detailed information about a specific wallet, including its balance.

    This method fetches the wallet's details using its unique identifier, along with the associated user and environment information.

    Args:
        wallet_id (str): The UUID of the wallet to be retrieved (required).
        params (dict): A dictionary of optional query parameters, which may include:
            environment_uuid (str): The UUID of the admin panel environment associated with the wallet.
            user_uuid (str): The UUID of the external system user associated with the wallet.

    Returns:
        dict: A dictionary containing the following fields:
            uuid (str): The UUID of the wallet.
            user_uuid (str): The UUID of the user associated with the wallet.
            status (dict): A dictionary representing the status of the wallet, containing:
                uuid (str): The UUID of the status.
                updated_at (datetime): The timestamp when the status was last updated.
                title (str): A human-readable title for the status.
                code (str): A code representing the status.
            balance (dict): A dictionary representing the wallet balance, containing:
                uuid (str): The UUID of the balance record.
                updated_at (datetime): The timestamp when the balance was last updated.
                iso_currency_code (str): The ISO 4217 currency code for the wallet's currency.
                current (int): The current balance amount in the specified currency.
            number (int): The wallet's unique identifier or number.
            created_at (datetime): The timestamp when the wallet was created.
            updated_at (datetime | None): The timestamp when the wallet was last updated, or None if not applicable.
            rewarding_balance (int): The current rewarding balance associated with the wallet.
            currency_uuid (str): The UUID of the currency used for the wallet.
    """
    return self.sign_request('wallet', 'GET', f'/wallet/{wallet_id}', params=params)
