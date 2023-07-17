"""Status APIs for Tessie."""


class Status:
    """Status class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def status(self, vin: str) -> str:
        """Get the status of the vehicle. The status may be asleep, waiting_for_sleep or awake.

        vin: VIN.
        """

        results = await self.client.http_get(f"{vin}/status", {})

        return results["status"]
