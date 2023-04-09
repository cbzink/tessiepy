"""A Python API for Tessie."""

from typing import Any
from aiohttp import ClientSession, ClientResponse

from .charging import Charging
from .current_state import CurrentState

from .exceptions import AuthenticationError, TessieError

API_URL = 'https://api.tessie.com'
API_TIMEOUT = 60 * 5

class TessieClient:
    """Tessie client."""

    def __init__(self, access_token: str, session: ClientSession | None = None) -> None:
        """Initialize Sensibo Client.

        access_token: Access token from Tessie.
        session: aiohttp.ClientSession or None to create a new session.
        """

        self.access_token = access_token
        self.timeout = API_TIMEOUT
        self._session = session if session else ClientSession()

        self.current_state = CurrentState(self)
        self.charging = Charging(self)


    async def get(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        """Perform a GET request to the Tessie API."""

        headers = {"Authorization": f"Bearer: {self.access_token}"}

        try:
            async with self._session.get(
                f"{API_URL}/{path}",
                params=params,
                timeout=self.timeout,
                headers=headers,
            ) as resp:
                return await self._response(resp)
        except Exception as error:
            raise error

    async def _response(self, resp: ClientResponse) -> dict[str, Any]:
        """Return response from an API call."""

        if resp.status == 401:
            raise AuthenticationError("Invalid Access Token")

        if resp.status != 200:
            error = await resp.text()

            raise TessieError(f"API Error: {error}")

        try:
            return await resp.json()
        except Exception as error:
            raise TessieError(f"JSON Parsing Failed: {error}") from error

