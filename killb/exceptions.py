
class KillBApiError(Exception):
    pass


class AuthenticationError(KillBApiError):
    pass


class NotFoundError(KillBApiError):
    pass
