"""Horn APIs for Tessie."""


class Horn:
    """Horn class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def honk(self, vin: str) -> None:
        """Honk the horn.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/honk", {})
