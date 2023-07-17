"""Sentry Mode APIs for Tessie."""


class SentryMode:
    """Sentry Mode class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def enable_sentry(self, vin: str) -> None:
        """Enable Sentry Mode.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/enable_sentry", {})

    async def disable_sentry(self, vin: str) -> None:
        """Disable Sentry Mode.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/disable_sentry", {})
