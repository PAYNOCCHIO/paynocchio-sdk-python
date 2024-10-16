# coding: utf-8

"""
    Paynocchio API

    The Paynocchio REST API. Please visit https://www.paynocchio.com

    Contact: developers@paynocchio.com
"""  # noqa: E501


def get_status(self) -> dict:
    """
    Get available statuses for Wallet

    Response:
        statuses: StatusListSchema(
            ListSchema(
            uuid: UUID
            updated_at: Datetime
            title: str
            code: str
            )
        )
    """
    return self.sign_request('wallet', 'GET', '/status')