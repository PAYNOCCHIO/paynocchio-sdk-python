def get_order_list(self, params: dict) -> dict:
    """
    Get order list.

    params:
        uuid: UUID4.
        created_at: datetime.
        wallet_uuid: UUID4.
        external_user_id: str.
        external_product_id: str.
        amount: int.
        status_order_uuid: UUID4.
        skip: int.
        limit: int.
    
    Response:
        id: str.
        created_at: datetime.
        wallet_id: str.
        user_id: str.
        product_id: UUID4.
        amount: float.
        status_code: str.
    """
    return self.sign_request('transaction', 'GET', '/wallet', params=params)


def get_order(self, params: dict) -> dict:
    """
    Get order by uuid.

    params:
        uuid: UUID4.
    
    Response:
        id: str.
        wallet_id: str.
        user_id: str.
        product_id: UUID4.
        amount: double.
        status_code: str.

    """
    return self.sign_request('transaction', 'GET', '/wallet', params=params)
