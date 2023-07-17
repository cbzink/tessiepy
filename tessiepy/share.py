"""Share APIs for Tessie."""


class Share:
    """Share class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def share(self, vin: str, value: str, locale: str = None) -> None:
        """Shares an address, latitude/longitude or video URL to the vehicle.

        vin: VIN.
        value: A street address, latitude/longitude coordinates or a video URL.
        locale: The language and country code locale of the address. Useful for helping addresses translate to the navigation system accurately.
        """

        params = {"value": value}

        if locale is not None:
            params["locale"] = locale

        await self.client.http_get(f"{vin}/command/share", params)
