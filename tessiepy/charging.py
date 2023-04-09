"""Charging APIs for Tessie."""

class Charging:
    """Charging class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def set_charge_limit(self, vin: str, percent: int) -> None:
        """Set charge limit for vehicle.

        vin: VIN.
        percent: Charge limit.
        """

        params = {"percent": percent}

        await self.client.get(f"{vin}/command/set_charge_limit", params)
