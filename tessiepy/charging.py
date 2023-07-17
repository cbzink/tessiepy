"""Charging APIs for Tessie."""


class Charging:
    """Charging class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def start_charging(self, vin: str) -> None:
        """Start charging.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/start_charging", {})

    async def stop_charging(self, vin: str) -> None:
        """Stop charging.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/stop_charging", {})

    async def set_charge_limit(self, vin: str, percent: int) -> None:
        """Set the charge limit.

        vin: VIN.
        percent: The battery percentage to charge to.
        """

        params = {"percent": percent}

        await self.client.http_get(f"{vin}/command/set_charge_limit", params)

    async def set_charging_amps(self, vin: str, amps: int) -> None:
        """Set the charge limit.

        vin: VIN.
        amps: The number of amps.
        """

        params = {"amps": amps}

        await self.client.http_get(f"{vin}/command/set_charging_amps", params)

    async def open_charge_port(self, vin: str) -> None:
        """Open the charge port if it's closed, or unlock it if it's open.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/open_charge_port", {})

    async def close_charge_port(self, vin: str) -> None:
        """Close the charge port.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/close_charge_port", {})
