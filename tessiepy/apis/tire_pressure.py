"""Tire Pressure APIs for Tessie."""

from tessiepy.models import TirePressureData


class TirePressure:
    """Tire Pressure class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def tire_pressure(self, vin: str) -> TirePressureData:
        """Get the tire pressure of the vehicle, measured in bar. Requires firmware 2022.4.5+.

        vin: VIN.
        """

        results = await self.client.http_get(f"{vin}/tire_pressure", {})

        return TirePressureData(
            front_left=results["front_left"],
            front_right=results["front_right"],
            rear_left=results["rear_left"],
            rear_right=results["rear_right"],
            front_left_status=results["front_left_status"],
            front_right_status=results["front_right_status"],
            rear_left_status=results["rear_left_status"],
            rear_right_status=results["rear_right_status"],
            timestamp=results["timestamp"],
        )
