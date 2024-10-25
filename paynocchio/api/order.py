# coding: utf-8

"""
    Paynocchio API

    The Paynocchio REST API. Please visit https://www.paynocchio.com

    Contact: developers@paynocchio.com
"""  # noqa: E501


def get_order(self, order_uuid: str, params: dict) -> dict:
    """
    Get an order by its UUID.

    This request fetches detailed information about a specific order using the order's UUID, user UUID, and wallet group UUID. The request includes signature validation and test mode switching via headers.

    params:
        environment_uuid: UUID Admin panel environment ID.
        user_uuid: UUID External system user id.

    Response:
        uuid: unique identifier of the order.
        wallet_uuid: unique identifier of the wallet linked to the order.
        external_user_id: external identifier of the user.
        external_order_id: external identifier of the order.
        request_uuid: identifier associated with the request.
        created_at: timestamp when the order was created.
        amount: the order amount.
        status: StatusSchema(
            uuid: UUID
            updated_at: Datetime
            title: str
            code: str
        )
        bonus_amount: bonus amount applied to the order.
        full_amount: total amount including bonuses.
    """
    return self.sign_request('order', 'GET', f'/orders/{order_uuid}', params=params)



def get_orders_by_wallet_uuid(self, params: dict) -> dict:

    """
    Fetches a list of orders associated with a specific wallet UUID.

    This function retrieves orders by making a signed request to the order service.
    The request is authenticated via the wallet signature and can optionally be toggled into test mode.

    params: dict
        A dictionary containing the following keys:
            environment_uuid (UUID): The unique identifier of the admin panel environment.
            user_uuid (UUID): The external system user's unique identifier.
            wallet_uuid (UUID): The external system wallet's unique identifier.
    """

    return self.sign_request('order', 'GET', f'/orders', params=params)
