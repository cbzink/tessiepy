"""Exceptions for Tessie."""

from typing import Any


class TessieError(Exception):
    """Error from Tessie API."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""

        Exception.__init__(self, *args)


class AuthenticationError(Exception):
    """Authentication error from Tessie API."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""

        Exception.__init__(self, *args)
