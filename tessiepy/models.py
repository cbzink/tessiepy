"""Data classes for Tessie."""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class TessieVehicle:
    """Dataclass for TessieVehicle."""

    vin: str
    display_name: str
    state: str
    in_service: bool
    charge_state: ChargeState
    drive_state: DriveState
    vehicle_config: VehicleConfig
    vehicle_state: VehicleState

@dataclass
class ChargeState:
    """Dataclass for ChargeState."""

    battery_level: int
    battery_range: float
    charge_limit_soc: int
    charge_limit_soc_max: int
    charge_limit_soc_min: int
    charge_port_latch: str
    charging_state: str

@dataclass
class DriveState:
    """Dataclass for DriveState."""

    latitude: float
    longitude: float

@dataclass
class VehicleConfig:
    """Dataclass for VehicleConfig."""

    car_type: str

@dataclass
class VehicleState:
    """Dataclass for VehicleState."""

    car_version: str
    vehicle_name: str
