"""A Python API for Tessie."""

import json

from typing import Any
from aiohttp import ClientSession, ClientResponse

from tessiepy.apis.current_state import CurrentState
from tessiepy.apis.drives import Drives
from tessiepy.apis.charges import Charges
from tessiepy.apis.idles import Idles
from tessiepy.apis.battery_health import BatteryHealth
from tessiepy.apis.tire_pressure import TirePressure
from tessiepy.apis.status import Status
from tessiepy.apis.wake import Wake
from tessiepy.apis.doors import Doors
from tessiepy.apis.trunks import Trunks
from tessiepy.apis.windows import Windows
from tessiepy.apis.climate import Climate
from tessiepy.apis.charging import Charging
from tessiepy.apis.lights import Lights
from tessiepy.apis.horn import Horn
from tessiepy.apis.homelink import HomeLink
from tessiepy.apis.keyless_driving import KeylessDriving
from tessiepy.apis.sunroof import Sunroof
from tessiepy.apis.sentry_mode import SentryMode
from tessiepy.apis.valet_mode import ValetMode
from tessiepy.apis.software import Software
from tessiepy.apis.scheduling import Scheduling
from tessiepy.apis.share import Share
from tessiepy.apis.boombox import Boombox

from .exceptions import AuthenticationError, TessieError

API_URL = "https://api.tessie.com"
API_TIMEOUT = 60 * 5
RETRY_DURATION = 40
WAIT_FOR_COMPLETION = True


class TessieClient:
    """Tessie client."""

    def __init__(self, access_token: str, session: ClientSession | None = None) -> None:
        """Initializes the Tessie Client.

        access_token: Access token from Tessie.
        session: aiohttp.ClientSession or None to create a new session.
        """

        self.access_token = access_token
        self.timeout = API_TIMEOUT
        self.retry_duration = RETRY_DURATION
        self.wait_for_completion = WAIT_FOR_COMPLETION
        self._session = session if session else ClientSession()

        self.current_state = CurrentState(self)

        self.drives = Drives(self)
        self.charges = Charges(self)
        self.idles = Idles(self)
        self.battery_health = BatteryHealth(self)
        self.tire_pressure = TirePressure(self)
        self.status = Status(self)
        self.wake = Wake(self)
        self.doors = Doors(self)
        self.trunks = Trunks(self)
        self.windows = Windows(self)
        self.climate = Climate(self)
        self.charging = Charging(self)
        self.lights = Lights(self)
        self.horn = Horn(self)
        self.homelink = HomeLink(self)
        self.keyless_driving = KeylessDriving(self)
        self.sunroof = Sunroof(self)
        self.sentry_mode = SentryMode(self)
        self.valet_mode = ValetMode(self)
        self.software = Software(self)
        self.scheduling = Scheduling(self)
        self.share = Share(self)
        self.boombox = Boombox(self)

    def set_retry_duration(self, retry_duration: int) -> None:
        """Sets the number of seconds commands will be attempted for.

        retry_duration: Number of seconds commands will be attempted for.
        """

        self.retry_duration = retry_duration

    def set_wait_for_completion(self, wait_for_completion: bool) -> None:
        """Sets if Tessie wait for the command to complete before responding.

        wait_for_completion: True to wait until the command completes before responding.
        """

        self.wait_for_completion = wait_for_completion

    def get_configuration(self) -> dict[str, Any]:
        """Returns query parameters for commands."""

        return {
            "retry_duration": self.retry_duration,
            "wait_for_completion": self.wait_for_completion,
        }

    async def http_get(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        """Performs a GET request to the Tessie API."""

        headers = {"Authorization": f"Bearer: {self.access_token}"}

        try:
            async with self._session.get(
                f"{API_URL}/{path}",
                params=params,
                timeout=self.timeout,
                headers=headers,
            ) as resp:
                return await self._http_response(resp)
        except Exception as error:
            raise error

    async def http_post_json(
        self, path: str, params: dict[str, Any], body: dict
    ) -> dict[str, Any]:
        """Performs a GET request to the Tessie API."""

        headers = {
            "Authorization": f"Bearer: {self.access_token}",
            "Content-Type": "application/json",
        }

        try:
            async with self._session.post(
                f"{API_URL}/{path}",
                params=params,
                data=json.dumps(body),
                timeout=self.timeout,
                headers=headers,
            ) as resp:
                return await self._http_response(resp)
        except Exception as error:
            raise error

    async def _http_response(self, resp: ClientResponse) -> dict[str, Any]:
        """Returns response from an API call."""

        if resp.status == 401:
            raise AuthenticationError("Invalid Access Token")

        if resp.status != 200:
            error = await resp.text()

            raise TessieError(f"API Error: {error}")

        try:
            return await resp.json()
        except Exception as error:
            raise TessieError(f"JSON Parsing Failed: {error}") from error
