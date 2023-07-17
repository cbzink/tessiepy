"""Windows APIs for Tessie."""


class Windows:
    """Windows class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def vent_windows(self, vin: str) -> None:
        """Vent all windows.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/vent_windows", {})

    async def close_windows(self, vin: str) -> None:
        """Close all windows, if the vehicle firmware supports it for the model and region.

        vin: VIN.
        """

        await self.client.http_get(f"{vin}/command/close_windows", {})
