"""Sentry APIs for Tessie."""

class Sentry:
    """Sentry class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def enable_sentry(self, vin: str) -> None:
        """Enable sentry

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/enable_sentry")

    async def disable_sentry(self, vin: str) -> None:
        """Disable sentry

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/disable_sentry")
