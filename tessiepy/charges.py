"""Charges APIs for Tessie."""

from .models import ChargeData


class Charges:
    """Charges class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def charges(self, vin: str, **kwargs) -> dict[int, ChargeData]:
        """Get the charges for the vehicle.

        Forces JSON format.

        vin: VIN.
        **kwargs: Additional params specified in https://developer.tessie.com/reference/get-charges.
        """

        params = {}

        for key, value in kwargs:
            if isinstance(value, bool):
                value = str(value).lower()

            params[key] = value

        params["format"] = "json"

        results = await self.client.http_get(f"{vin}/charges", params)

        response = {}

        for charge in results["results"]:
            response[charge["id"]] = ChargeData(
                id=charge["id"],
                started_at=charge["started_at"],
                ended_at=charge["ended_at"],
                created_at=charge["created_at"],
                updated_at=charge["updated_at"],
                location=charge["location"],
                latitude=charge["latitude"],
                longitude=charge["longitude"],
                is_supercharger=charge["is_supercharger"],
                odometer=charge["odometer"],
                energy_added=charge["energy_added"],
                energy_used=charge["energy_used"],
                miles_added=charge["miles_added"],
                miles_added_ideal=charge["miles_added_ideal"],
                starting_battery=charge["starting_battery"],
                ending_battery=charge["ending_battery"],
                cost=charge["cost"],
            )

        return response

    async def set_cost(self, vin: str, charge_id: int, cost: float = None) -> None:
        """Sets the cost of a charge.

        vin: VIN.
        charge_id: The ID of the charge.
        cost: The cost of the charge. Leave empty to remove the cost.
        """

        params = {}

        if cost is not None:
            params["cost"] = cost

        await self.client.http_get(f"{vin}/charges/{charge_id}/set_cost", params)
