"""Wake APIs for Tessie."""


class Wake:
    """Wake class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def wake(self, vin: str) -> None:
        """Wake the vehicle from sleep.

        TODO: Implement better success/timeout handling.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/wake", {})
