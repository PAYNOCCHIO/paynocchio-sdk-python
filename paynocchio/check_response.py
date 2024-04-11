from paynocchio.exceptions import exception_status_code
from requests import Response


def exception_catch(api: str, response: Response) -> None:
    status_code = response.status_code
    exception_status_code(api, status_code)
