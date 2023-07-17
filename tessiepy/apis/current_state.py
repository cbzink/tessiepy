"""Current State APIs for Tessie."""

from tessiepy.models import LocationData, WeatherData


class CurrentState:
    """Current State class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def state(self, vin: str, use_cache: bool = True) -> dict:
        """Get the latest state of the vehicle.

        If use_cache is true (default), this call always returns a complete set of data and doesn't impact vehicle sleep. If the vehicle is awake, the data is usually less than 10 seconds old. If the vehicle is asleep, the data is from the time the vehicle went to sleep.

        If use_cache is false, this call retrieves data using a live connection, which may return {"state": "asleep"} or network errors depending on vehicle connectivity.

        See https://developer.tessie.com/reference/get-state for response data.

        use_cache: Whether to return the most recently seen data.
        """

        params = {"use_cache": str(use_cache).lower()}

        results = await self.client.http_get(f"{vin}/state", params)

        return results

    async def vehicles(self, only_active: bool = False) -> dict:
        """Get all vehicles and their latest state.

        This call always returns a complete set of data and doesn't impact vehicle sleep. If the vehicle is awake, the data is usually less than 10 seconds old. If the vehicle is asleep, the data is from the time the vehicle went to sleep.

        See https://developer.tessie.com/reference/get-vehicles for response data.

        only_active: Whether to include only active, unarchived vehicles in the response.
        """

        params = {"only_active": str(only_active).lower()}

        results = await self.client.http_get("vehicles", params)

        return results["results"]

    async def location(self, vin: str) -> LocationData:
        """Get the coordinates, street address and associated saved location of the vehicle.

        vin: VIN.
        """

        results = await self.client.http_get(f"{vin}/location", {})

        return LocationData(
            latitude=results["latitude"],
            longitude=results["longitude"],
            address=results["address"],
            saved_location=results["saved_location"],
        )

    async def weather(self, vin: str) -> WeatherData:
        """Get the weather forecast around the vehicle.

        vin: VIN.
        """

        results = await self.client.http_get(f"{vin}/weather", {})

        return WeatherData(
            location=results["location"],
            condition=results["condition"],
            temperature=results["temperature"],
            feels_like=results["feels_like"],
            humidity=results["humidity"],
            visibility=results["visibility"],
            pressure=results["pressure"],
            sunrise=results["sunrise"],
            sunset=results["sunset"],
            cloudiness=results["cloudiness"],
            wind_speed=results["wind_speed"],
            wind_direction=results["wind_direction"],
        )
