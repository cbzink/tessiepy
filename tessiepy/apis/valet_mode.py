"""Valet Mode APIs for Tessie."""


class ValetMode:
    """Valet Mode class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def enable_valet(self, vin: str) -> None:
        """Enable Valet Mode.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/enable_valet", {})

    async def disable_valet(self, vin: str) -> None:
        """Disable Valet Mode.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/disable_valet", {})
