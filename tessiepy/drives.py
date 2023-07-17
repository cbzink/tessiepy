"""Drives APIs for Tessie."""

from .models import DriveData


class Drives:
    """Drives class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def drives(self, vin: str, **kwargs) -> dict[int, DriveData]:
        """Get the drives for the vehicle.

        Forces JSON format.

        TODO: Support undocumented safety score fields.

        vin: VIN.
        **kwargs: Additional params specified in https://developer.tessie.com/reference/get-drives.
        """

        params = {}

        for key, value in kwargs:
            if isinstance(value, bool):
                value = str(value).lower()

            params[key] = value

        params["format"] = "json"

        results = await self.client.http_get(f"{vin}/drives", params)

        response = {}

        for drive in results["results"]:
            response[drive["id"]] = DriveData(
                id=drive["id"],
                started_at=drive["started_at"],
                ended_at=drive["ended_at"],
                created_at=drive["created_at"],
                updated_at=drive["updated_at"],
                starting_location=drive["starting_location"],
                starting_latitude=drive["starting_latitude"],
                starting_longitude=drive["starting_longitude"],
                starting_odometer=drive["starting_odometer"],
                ending_location=drive["ending_location"],
                ending_latitude=drive["ending_latitude"],
                ending_longitude=drive["ending_longitude"],
                ending_odometer=drive["ending_odometer"],
                starting_battery=drive["starting_battery"],
                ending_battery=drive["ending_battery"],
                average_inside_temperature=drive["average_inside_temperature"],
                average_outside_temperature=drive["average_outside_temperature"],
                average_speed=drive["average_speed"],
                max_speed=drive["max_speed"],
                rated_range_used=drive["rated_range_used"],
                odometer_distance=drive["odometer_distance"],
                energy_used=drive["energy_used"],
                tag=drive["tag"],
            )

        return response

    async def path(self, vin: str, _from: int = None, _to: int = None) -> list:
        """Get the driving path of the vehicle during a given timeframe. If no timeframe is specified, returns the driving path for the last 30 days.

        vin: VIN.
        _from: The start of the timeframe. Unix timestamp in seconds.
        _to: The end of the timeframe. Unix timestamp in seconds.
        """
        params = {}

        if _from is not None:
            params["from"] = _from

        if _to is not None:
            params["to"] = _to

        results = await self.client.http_get(f"{vin}/path", params)

        return results["results"]

    async def set_tag(self, vin: str, drives: list, tag: str) -> None:
        """Sets the tag for a list of drives.

        vin: VIN.
        drives: A list of drive IDs.
        tag: The tag to apply to the drives.
        """

        body = {"tag": tag, "drives": str.join(",", map(str, drives))}

        await self.client.http_post_json(f"{vin}/drives/set_tag", {}, body)
