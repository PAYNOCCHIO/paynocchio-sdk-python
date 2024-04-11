def get_status(self) -> dict:
    """
    To get list of statusses.

    Response:
        statusses:
            list[
            {
                uuid: UUID4.
                updated_at: datetime.
                title: str.
                code: str.
            }
            ]
        
    """
    return self.sign_request('wallet', 'GET', '/status')
