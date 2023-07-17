"""Keyless Driving APIs for Tessie."""


class KeylessDriving:
    """Keyless Driving class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def remote_start(self, vin: str) -> None:
        """Enable keyless driving. Driving must begin within 2 minutes.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/remote_start", {})
