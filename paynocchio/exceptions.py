class ServerError(Exception):
    def __init__(self):
        self.text = 'Server internal error'


class FieldRequiredError(Exception):
    def __init__(self):
        self.text = 'Missing field reuired error'


status_bad = {
    'wallet': {
        500: ServerError,
        422: FieldRequiredError,
    },
}


def exception_status_code(api: str, status_sode: int) -> None:
    if status_sode not in [200, 201, 203, 204]:
        exception = status_bad[api][status_sode]
        raise exception()