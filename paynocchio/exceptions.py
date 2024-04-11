class ServerError(Exception):
    def __init__(self):
        self.text = 'Server internal error'


class FieldRequiredError(Exception):
    def __init__(self):
        self.text = 'Missing field reuired error'


class ResponseError(Exception):
    def __init__(self):
        self.text = 'Response error'


status_bad = {
    'wallet': {
        500: ServerError,
        422: FieldRequiredError,
        400: ResponseError,
    },
    'transaction': {
        500: ServerError,
        422: FieldRequiredError,
        400: ResponseError,
    },
}


def exception_status_code(api: str, status_sode: int) -> None:
    if status_sode not in [200, 201, 203, 204]:
        exception = status_bad.get(api, {}).get(status_sode, ResponseError)
        raise exception()