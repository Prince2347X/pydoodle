class LanguageNotSupported(Exception):
    """Raised if wrong language code is provided."""
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
