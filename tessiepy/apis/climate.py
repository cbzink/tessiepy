"""Climate APIs for Tessie."""


class Climate:
    """Climate class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def start_climate(self, vin: str) -> None:
        """Starts the climate system and preconditions the battery.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/start_climate", {})

    async def stop_climate(self, vin: str) -> None:
        """Stops the climate system.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/stop_climate", {})

    async def set_temperatures(self, vin: str, temperature: float) -> None:
        """Set the cabin temperature.

        vin: VIN.
        temperature: The temperature in Celsius.
        """

        params = {"temperature": temperature}

        await self.client.http_get(f"{vin}/command/set_temperatures", params)

    async def set_seat_heat(self, vin: str, seat: str, level: int = None) -> None:
        """Control a seat heater.

        vin: VIN.
        seat: The name of the seat. Set to "all" to start all seat heaters.
        level: The heat level. Set to 0 to turn off.
        """

        params = {"seat": seat}

        if level is not None:
            params["level"] = level

        await self.client.http_get(f"{vin}/command/set_seat_heat", params)

    async def start_max_defrost(self, vin: str) -> None:
        """Start defrosting.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/start_max_defrost", {})

    async def stop_max_defrost(self, vin: str) -> None:
        """Stop defrosting.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/stop_max_defrost", {})

    async def start_steering_wheel_heater(self, vin: str) -> None:
        """Start the steering wheel heater.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/start_steering_wheel_heater", {})

    async def stop_steering_wheel_heater(self, vin: str) -> None:
        """Stop the steering wheel heater.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/stop_steering_wheel_heater", {})

    async def set_bioweapon_mode(self, vin: str, on: bool) -> None:
        """Control Bioweapon Defense Mode.

        vin: VIN.
        on: Whether to enable Bioweapon Defense Mode.
        """

        params = {"on": str(on).lower()}

        await self.client.http_get(f"{vin}/command/set_bioweapon_mode", params)

    async def set_climate_keeper_mode(self, vin: str, mode: int) -> None:
        """Set the Climate Keeper mode.

        vin: VIN.
        mode: The Climate Keeper mode. Use 2 for Dog Mode, 3 for Camp Mode, 0 to disable.
        """

        params = {"mode": mode}

        await self.client.http_get(f"{vin}/command/set_climate_keeper_mode", params)
