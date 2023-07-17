"""Sunroof APIs for Tessie."""


class Sunroof:
    """Sunroof class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def vent_sunroof(self, vin: str) -> None:
        """Vent the sunroof.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/vent_sunroof", {})

    async def close_sunroof(self, vin: str) -> None:
        """Close the sunroof.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/close_sunroof", {})
