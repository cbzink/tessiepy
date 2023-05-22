"""Doors APIs for Tessie."""


class Doors:
    """Doors class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def lock(self, vin: str) -> None:
        """Locks the doors

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/lock")

    async def unlock(self, vin: str) -> None:
        """Unlocks the doors

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/unlock")
