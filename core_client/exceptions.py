"""Typed exceptions for the client.

By default the API methods return either a response model or an ``Error`` model,
so callers must type-check the result. Passing ``raise_on_error=True`` to the
client turns any ``Error`` response into a ``CoreAPIError`` instead
(CLIENT-TODO §2.6).
"""

from httpx import HTTPError

from .base.models import Error


class CoreAPIError(HTTPError):
    """Raised when an API call returns an ``Error`` and ``raise_on_error`` is on.

    The original ``Error`` model is available as ``.error`` (and its ``code`` /
    ``message`` are copied onto the exception for convenience).
    """

    def __init__(self, error: Error):
        self.error = error
        self.code = error.code
        self.message = error.message
        super().__init__(f"{error.code}: {error.message}")
