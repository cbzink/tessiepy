"""Wake APIs for Tessie."""


class Wake:
    """Wake class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def wake_vehicle(self, vin: str) -> bool:
        """Wakes the vehicle.

        vin: VIN.
        """

        return await self.client.get(f"{vin}/wake")
