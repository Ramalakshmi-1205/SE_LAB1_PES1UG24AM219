
import pytest

from irrigation_scheduler import should_irrigate, water_volume, schedule


def test_wet_soil_no_irrigation():
    assert should_irrigate(70, 0, "seedling") is False


def test_seedling_volume():
    assert water_volume(10, "seedling", 20) == 20


# should_irrigate tests

def test_rainfall_too_high():
    assert should_irrigate(30, 10, "seedling") is False


def test_seedling_dry_soil():
    assert should_irrigate(30, 0, "seedling") is True


def test_seedling_moisture_boundary():
    assert should_irrigate(45, 0, "seedling") is False


def test_flowering_needs_water():
    assert should_irrigate(50, 0, "flowering") is True


def test_flowering_moisture_boundary():
    assert should_irrigate(55, 0, "flowering") is False


def test_other_stage_dry_soil():
    assert should_irrigate(30, 0, "fruiting") is True


def test_other_stage_moderate_rain():
    assert should_irrigate(30, 5, "fruiting") is False


def test_other_stage_moisture_boundary():
    assert should_irrigate(40, 0, "fruiting") is False


# water_volume tests

def test_flowering_volume():
    assert water_volume(10, "flowering", 20) == 50


def test_other_stage_volume():
    assert water_volume(10, "fruiting", 20) == 40


def test_zero_area_raises_error():
    with pytest.raises(ValueError, match="invalid area"):
        water_volume(0, "seedling", 20)


def test_negative_area_raises_error():
    with pytest.raises(ValueError, match="invalid area"):
        water_volume(-2, "seedling", 20)


def test_hot_weather_increases_volume():
    assert water_volume(10, "seedling", 36) == 30


def test_cold_weather_reduces_volume():
    assert water_volume(10, "seedling", 9) == 10


def test_temperature_boundaries():
    assert water_volume(10, "seedling", 35) == 20
    assert water_volume(10, "seedling", 10) == 20


# schedule tests

def test_schedule_adds_irrigated_zone():
    zones = [("Zone A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 100) == ["Zone A"]


def test_schedule_skips_zone_not_needing_water():
    zones = [("Zone A", 10, 70, 0, "seedling", 20)]
    assert schedule(zones, 100) == []


def test_schedule_stops_when_budget_is_insufficient():
    zones = [
        ("Zone A", 10, 30, 0, "seedling", 20),
        ("Zone B", 10, 30, 0, "seedling", 20),
    ]
    assert schedule(zones, 15) == []


def test_schedule_uses_remaining_budget():
    zones = [
        ("Zone A", 5, 30, 0, "seedling", 20),
        ("Zone B", 5, 30, 0, "seedling", 20),
    ]
    assert schedule(zones, 20) == ["Zone A", "Zone B"]


def test_schedule_empty_zones():
    assert schedule([], 100) == []
