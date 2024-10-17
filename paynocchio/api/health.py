# coding: utf-8

"""
    Paynocchio API

    The Paynocchio REST API. Please visit https://www.paynocchio.com

    Contact: developers@paynocchio.com
"""  # noqa: E501


def get_health(self) -> dict:
    """
    Check Database Health Status.

    This method is used to check the health status of the database. It performs a simple health check to ensure that the database connection is functional and responsive.

    Returns:
        dict: A dictionary containing the database health status:
            - **database** (str): A string indicating the health of the database. Possible value:
                - `"ok"`: The database is functioning properly.

    Example Response:
        {
            "database": "ok"
        }
    """
    return self.sign_request('health', 'GET', '/health')



def check_signature(self, data: dict) -> dict:
    """
    Validate API Key and Environment.

    This method checks whether the provided API key and environment UUID are valid for integration purposes. It ensures that the API key is recognized and that the environment is correctly configured.

    Parameters:
        data (dict): A dictionary containing the following keys:
            - **environment_uuid** (UUID): The unique identifier for the environment where the API call is being made.
            - **secret_key** (UUID): The API key used for authentication.

    Returns:
        dict: A dictionary containing the integration status:
            - **integration_status** (str): HTTP status code indicating the result of the validation (e.g., "200").
            - **message** (str): A message providing additional context, typically confirming successful validation (e.g., "Integration is approved").
            - **status_code** (int): The HTTP status code of the response.

    Example Response:
        {
            "integration_status": "200",
            "message": "Integration is approved",
            "status_code": 200
        }
    """
    return self.sign_request('health', 'POST', '/healthcheck', body_data=data)
