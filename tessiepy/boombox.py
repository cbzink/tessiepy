"""Boombox APIs for Tessie."""


class Boombox:
    """Boombox class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def remote_boombox(self, vin: str) -> None:
        """Generates a fart sound. Requires 2022.40.25+.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/remote_boombox", {})
