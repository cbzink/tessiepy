"""Lights APIs for Tessie."""


class Lights:
    """Lights class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def flash(self, vin: str) -> None:
        """Flash the lights.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/flash", {})
