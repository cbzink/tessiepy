"""Scheduling APIs for Tessie."""


class Scheduling:
    """Scheduling class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def set_scheduled_charging(self, vin: str, enable: bool, time: int) -> None:
        """Set the scheduled charging configuration.

        vin: VIN.
        enable: Whether to enable scheduled charging.
        time: The minutes past midnight local time to start charging.
        """

        params = {"enable": str(enable).lower(), "time": time}

        await self.client.http_get(f"{vin}/command/set_scheduled_charging", params)

    async def set_scheduled_departure(
        self, vin: str, enable: bool, departure_time: int, **params
    ) -> None:
        """Set the scheduled departure configuration.

        vin: VIN.
        enable: Whether to enable scheduled departure.
        departure_time: The departure time in minutes past midnight local time.
        **params: Additional params specified in https://developer.tessie.com/reference/set-scheduled-departure.
        """

        for key, value in params.items():
            if isinstance(value, bool):
                params[key] = str(value).lower()

        params.update({"enable": str(enable).lower(), "departure_time": departure_time})

        await self.client.http_get(f"{vin}/command/set_scheduled_departure", params)
