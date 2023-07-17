"""Doors APIs for Tessie."""


class Doors:
    """Doors class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def lock(self, vin: str) -> None:
        """Lock the vehicle.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/lock", {})

    async def unlock(self, vin: str) -> None:
        """Unlock the vehicle.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/unlock", {})
