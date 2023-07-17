"""Software APIs for Tessie."""


class Software:
    """Software class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def schedule_software_update(self, vin: str, in_seconds: int) -> None:
        """Schedule a software update.

        vin: VIN.
        in_seconds: The number of seconds in the future to schedule the update for. Set to 0 to schedule the update immediately.
        """

        params = {"in_seconds": in_seconds}

        await self.client.http_get(f"{vin}/command/schedule_software_update", params)

    async def cancel_software_update(self, vin: str) -> None:
        """Cancel any scheduled software update.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/cancel_software_update", {})
