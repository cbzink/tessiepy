"""Idles APIs for Tessie."""

from .models import IdleData


class Idles:
    """Idles class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def idles(self, vin: str, **kwargs) -> dict[int, IdleData]:
        """Get the idles for the vehicle. The vehicle is considered idle if parked and unplugged.

        Forces JSON format.

        vin: VIN.
        **kwargs: Additional params specified in https://developer.tessie.com/reference/get-idles.
        """

        params = {}

        for key, value in kwargs:
            if isinstance(value, bool):
                value = str(value).lower()

            params[key] = value

        params["format"] = "json"

        results = await self.client.http_get(f"{vin}/idles", params)

        response = {}

        for idle in results["results"]:
            response[idle["id"]] = IdleData(
                id=idle["id"],
                started_at=idle["started_at"],
                ended_at=idle["ended_at"],
                created_at=idle["created_at"],
                updated_at=idle["updated_at"],
                location=idle["location"],
                latitude=idle["latitude"],
                longitude=idle["longitude"],
                starting_battery=idle["starting_battery"],
                ending_battery=idle["ending_battery"],
                rated_range_used=idle["rated_range_used"],
                ideal_range_used=idle["ideal_range_used"],
                climate_fraction=idle["climate_fraction"],
                sentry_fraction=idle["sentry_fraction"],
                energy_used=idle["energy_used"],
            )

        return response
