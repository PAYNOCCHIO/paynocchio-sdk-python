# coding: utf-8

"""
    Paynocchio API

    The Paynocchio REST API. Please visit https://www.paynocchio.com

    Contact: developers@paynocchio.com
"""  # noqa: E501


def get_status(self) -> dict:
    """
    Retrieves the available statuses for the wallet.

    This method fetches a list of status objects that represent the various states a wallet can be in.

    Returns:
        dict: A dictionary containing the following key:
            **statuses** (list): A list of status objects, each containing:
                **uuid** (str): The unique identifier for the status.
                **updated_at** (str, ISO 8601 format): The date and time when the status was last updated.
                **title** (str): A human-readable title describing the status.
                **code** (str): A machine-readable code representing the status.
    """
    return self.sign_request('wallet', 'GET', '/status')