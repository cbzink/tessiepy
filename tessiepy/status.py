"""Status APIs for Tessie."""


class Status:
    """Status class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def status(self, vin: str) -> str:
        """Status

        vin: VIN.

        returns: asleep, waiting_for_sleep or awake.
        """

        return await self.client.get(f"{vin}/status")
