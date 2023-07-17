"""Battery Health APIs for Tessie."""

from .models import BatteryHealthData


class BatteryHealth:
    """Battery Health class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def battery_health(self, vin: str) -> BatteryHealthData:
        """Get the calculated battery health of the vehicle.

        TODO: Support querying by timeframe.

        vin: VIN.
        """

        results = await self.client.http_get(f"{vin}/battery_health", {})

        return BatteryHealthData(
            max_range=results["result"]["max_range"],
            max_ideal_range=results["result"]["max_ideal_range"],
            capacity=results["result"]["capacity"],
        )
