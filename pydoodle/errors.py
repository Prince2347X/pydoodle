class LanguageNotSupported(Exception):
    """Raised if wrong language code is provided."""
    pass


class LimitExceeded(Exception):
    """Raised when the daily limit has exceeded. Learn more: https://jdoodle.com/compiler-api"""
    pass


class UnauthorizedRequest(Exception):
    """Raised if either your clientID or clientSecret is invalid."""
    pass


class BadRequest(Exception):
    """Raised when invalid language or versionIndex is provided. """
    pass


class LinkNotSupported(Exception):
    """Raised if the provided link isn't supported yet by pydoodle."""
    pass
