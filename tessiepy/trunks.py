"""Trunks APIs for Tessie."""


class Trunks:
    """Trunks class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def activate_front_trunk(self, vin: str) -> None:
        """Open the front trunk.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/activate_front_trunk", {})

    async def activate_rear_trunk(self, vin: str) -> None:
        """Open the rear trunk, or close it if the trunk is open and the vehicle has a powered trunk.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/activate_rear_trunk", {})
