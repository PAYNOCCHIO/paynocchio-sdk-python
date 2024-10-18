# coding: utf-8

"""
    Paynocchio API

    The Paynocchio REST API. Please visit https://www.paynocchio.com

    Contact: developers@paynocchio.com
"""  # noqa: E501

def topup_wallet(self, data: dict) -> dict:
    """
    Initiates the process to top up a user's wallet with a specified amount using a bank card.

    Parameters:
        data (dict): A dictionary containing the following required keys:
            environment_uuid (UUID): The unique identifier of the wallet group where the operation is performed.
            user_uuid (UUID): The unique identifier of the user whose wallet will be credited.
            wallet_uuid (UUID): The unique identifier of the wallet to be credited.
            amount (float): The amount of money to be added to the wallet.
            redirect_url (str): The URL to redirect the user to after the top-up process is completed.

    Returns:
        dict: A dictionary representing the response from the top-up request, typically structured as follows:
            id (str): The unique identifier for the payment link (e.g., "plink_1QAX8kPuDcQQWLF5sosdqFjP").
            currency (str): The currency used for the transaction (e.g., "usd").
            metadata (dict): Additional details regarding the transaction:
                amount (str): The amount to be added, in the smallest currency unit (e.g., "10000" for $100.00).
                company_id (UUID): The unique identifier of the company handling the transaction.
                company_stripe_account (str): The associated Stripe account (e.g., "acct_1QAB4bPuDcQQWLF5").
                currency (str): The currency in which the transaction will be processed (e.g., "USD").
                environment_uuid (UUID): The unique identifier of the wallet group where the transaction occurs.
                interaction_method (str): The method used for the transaction (e.g., "web").
                payment_request_uuid (UUID): A unique identifier for the payment request.
                stripe_product_id (str): The identifier for the Stripe product associated with the top-up.
                type_operation (str): The type of operation being performed (e.g., "payment_operation_add_money").
                user_uuid (UUID): The unique identifier of the user initiating the top-up.
                wallet_uuid (UUID): The unique identifier of the wallet to be credited.
                x_forwarded_for (str): The IP address from which the request originated.
                x_test_mode_switch (str): Indicates whether test mode is enabled (e.g., "on").
            url (str): The URL for the payment page (e.g., "https://buy.stripe.com/test_7sIdUOcKUgPAeQgfZ5").
            type_interactions (str): Describes the type of interaction (e.g., "success.interaction").
            interaction (str): The payment provider used for the transaction (e.g., "stripe").
    """
    return self.sign_request('operation', 'POST', '/operation/topup', body_data=data)



def payment_wallet(self, data: dict) -> dict:
    """
    Initiates a payment from a user's wallet for customer services.

    Parameters:
        data (dict): A dictionary containing the following keys:
            environment_uuid (UUID): The unique identifier of the wallet group where the payment is made.
            user_uuid (UUID): The unique identifier of the user making the payment.
            wallet_uuid (UUID): The unique identifier of the user's wallet to be charged.
            external_order_id (UUID): A unique identifier for the external order related to the payment.
            amount (float): The primary amount to be charged from the wallet.
            full_amount (float): The total amount for the transaction, which could include bonuses or other adjustments.
            bonus_amount (float): Any additional bonus amount applied to the transaction.

    Returns:
        dict: A dictionary representing the response from the payment request, structured as follows:
            schemas (dict): Details of the payment, including:
                amount (float): The amount charged from the wallet.
                card_uuid (UUID): The unique identifier of the card used for the payment.
                external_order_id (UUID): A unique identifier for the external order processed in the payment.
                full_amount (float): The total amount of the transaction.
                bonus_amount (float): Any bonus amount applied to the transaction.
            type_interactions (str): Describes the type of interaction (e.g., "success.interaction").
            interaction (str): The payment provider used for the transaction (e.g., "stripe").
    """
    return self.sign_request('operation', 'POST', '/operation/payment', body_data=data)


def withdraw_wallet(self, data: dict) -> dict:
    """
    Initiates a withdrawal from the user's wallet.

    Parameters:
        data (dict): A dictionary containing the following keys:
            environment_uuid (str): The unique identifier for the wallet group where the transaction is made.
            user_uuid (str): The unique identifier for the user requesting the withdrawal.
            wallet_uuid (str): The unique identifier for the user's wallet from which the funds are to be withdrawn.
            currency (str): The ISO 4217 3-letter code for the transaction currency (e.g., "USD").
            amount (float): The amount of money to be withdrawn from the wallet. Must be a positive value.

    Returns:
        dict: A dictionary containing the following keys:
            schemas (dict): Details of the withdrawal transaction:
                environment_uuid (str): The unique identifier of the wallet group.
                user_uuid (str): The unique identifier of the user.
                wallet_uuid (str): The unique identifier of the wallet used for the withdrawal.
                type_operation (str): The type of operation performed, in this case "payment_operation_withdraw".
                currency (str): The ISO 4217 3-letter currency code for the transaction.
                amount (float): The transaction amount that was withdrawn.
                x_forwarded_for (str): The IP address from which the request was made.
            type_interactions (str): A description of the interaction type, e.g., "success.interaction".
            interaction (str): The payment provider used for the transaction, e.g., "stripe".
    """
    return self.sign_request('operation', 'POST', '/operation/withdraw', body_data=data)

