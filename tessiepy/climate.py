"""Climate APIs for Tessie."""


class Climate:
    """Climate class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def start_climate(self, vin: str) -> None:
        """Starts climate

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/start_climate")

    async def stop_climate(self, vin: str) -> None:
        """Stop climate

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/stop_climate")

    async def set_temperature(self, vin: str, temperature: int) -> None:
        """Sets the temperature

        vin: VIN.
        temperature: Temperature in Celcius
        """

        params = {"temperature": temperature}

        await self.client.get(f"{vin}/command/set_temperatures", params)

    async def start_max_defrost(self, vin: str) -> None:
        """Starts defrost

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/start_max_defrost")

    async def stop_max_defrost(self, vin: str) -> None:
        """Stop defrost

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/stop_max_defrost")

    async def start_steering_wheel_heater(self, vin: str) -> None:
        """Starts steering wheel heater

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/start_steering_wheel_heater")

    async def stop_steering_wheel_heater(self, vin: str) -> None:
        """Stop steering wheel heater

        vin: VIN.
        """

        await self.client.get(f"{vin}/command/stop_steering_wheel_heater")
