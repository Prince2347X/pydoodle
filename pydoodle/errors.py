class LanguageNotSupported(Exception):
    pass


class UnauthorizedRequest(Exception):
    """Raised if either your clientID or clientSecret is invalid."""
    pass


class BadRequest(Exception):
    """Raised when invalid language or versionIndex is provided. """
    pass
