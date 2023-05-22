"""Current State APIs for Tessie."""

from .models import (
    TessieVehicle,
    ChargeState,
    DriveState,
    VehicleConfig,
    VehicleState,
    ClimateState
)


class CurrentState:
    """Current State class."""

    def __init__(self, client) -> None:
        """Initialize the class."""

        self.client = client

    async def vehicles(self, only_active=False) -> dict[str, TessieVehicle]:
        """Get all vehicles from Tessie.
        
        only_active: Whether to include only active, unarchived vehicles in the response.
        """

        params = {"only_active": str(only_active).lower()}

        results = await self.client.get('vehicles', params)

        response = {}

        for vehicle in results['results']:
            _state = vehicle["last_state"]
            _charge_state = _state["charge_state"]
            _drive_state = _state["drive_state"]
            _vehicle_config = _state["vehicle_config"]
            _vehicle_state = _state["vehicle_state"]
            _climate_state = _state["climate_state"]

            response[vehicle["vin"]] = TessieVehicle(
                vin=vehicle["vin"],
                display_name=_state["display_name"],
                state=_state["state"],
                in_service=_state["in_service"],
                charge_state=ChargeState(
                    battery_level=_charge_state["battery_level"],
                    battery_range=_charge_state["battery_range"],
                    charge_limit_soc=_charge_state["charge_limit_soc"],
                    charge_limit_soc_max=_charge_state["charge_limit_soc_max"],
                    charge_limit_soc_min=_charge_state["charge_limit_soc_min"],
                    charge_port_latch=_charge_state["charge_port_latch"],
                    charging_state=_charge_state["charging_state"],
                ),
                drive_state=DriveState(
                    latitude=_drive_state["latitude"],
                    longitude=_drive_state["longitude"],
                ),
                vehicle_config=VehicleConfig(
                    car_type=_vehicle_config["car_type"],
                ),
                vehicle_state=VehicleState(
                    car_version=_vehicle_state["car_version"],
                    vehicle_name=_vehicle_state["vehicle_name"],
                ),
                climate_state=ClimateState(
                    inside_temp=_climate_state["inside_temp"],
                    outside_temp=_climate_state["outside_temp"],
                ),
            )

        return response
