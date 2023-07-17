"""HomeLink APIs for Tessie."""


class HomeLink:
    """HomeLink class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def trigger_homelink(self, vin: str) -> None:
        """Trigger the primary HomeLink device.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/trigger_homelink", {})
