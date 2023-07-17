"""Data classes for Tessie."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class LocationData:
    """Dataclass for Location"""

    latitude: float
    longitude: float
    address: str
    saved_location: str


@dataclass
class WeatherData:
    """Dataclass for Weather"""

    location: str
    condition: str
    temperature: float
    feels_like: float
    humidity: int
    visibility: int
    pressure: int
    sunrise: int
    sunset: int
    cloudiness: int
    wind_speed: float
    wind_direction: int


@dataclass
class TirePressureData:
    """Dataclass for Tire Pressure"""

    front_left: float
    front_right: float
    rear_left: float
    rear_right: float
    front_left_status: str
    front_right_status: str
    rear_left_status: str
    rear_right_status: str
    timestamp: int


@dataclass
class BatteryHealthData:
    """Dataclass for Battery Health"""

    max_range: float
    max_ideal_range: float
    capacity: float


@dataclass
class IdleData:
    """Dataclass for Idle"""

    id: int
    started_at: int
    ended_at: int
    created_at: int
    updated_at: int
    location: str
    latitude: float
    longitude: float
    starting_battery: int
    ending_battery: int
    rated_range_used: float
    ideal_range_used: float
    climate_fraction: float
    sentry_fraction: float
    energy_used: float


@dataclass
class ChargeData:
    """Dataclass for Charge"""

    id: int
    started_at: int
    ended_at: int
    created_at: int
    updated_at: int
    location: str
    latitude: float
    longitude: float
    is_supercharger: bool
    odometer: float
    energy_added: float
    energy_used: float
    miles_added: int
    miles_added_ideal: int
    starting_battery: int
    ending_battery: int
    cost: float


@dataclass
class DriveData:
    """Dataclass for Drive"""

    id: int
    started_at: int
    ended_at: int
    created_at: int
    updated_at: int
    starting_location: str
    starting_latitude: float
    starting_longitude: float
    starting_odometer: float
    ending_location: str
    ending_latitude: float
    ending_longitude: float
    ending_odometer: float
    starting_battery: int
    ending_battery: int
    average_inside_temperature: float
    average_outside_temperature: float
    average_speed: int
    max_speed: int
    rated_range_used: float
    odometer_distance: int
    energy_used: float
    tag: str
