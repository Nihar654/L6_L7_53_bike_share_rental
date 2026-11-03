import pytest
from bike_share_rental import ride_cost, dock_status, can_unlock


# ---------------- RIDE COST ----------------

def test_unknown_bike():
    with pytest.raises(ValueError):
        ride_cost("invalid", 30, False, False)


def test_valid_bike():
    assert ride_cost("standard", 30, False, False) == 20


def test_invalid_duration_zero():
    with pytest.raises(ValueError):
        ride_cost("standard", 0, False, False)


def test_invalid_duration_negative():
    with pytest.raises(ValueError):
        ride_cost("standard", -10, False, False)


def test_subscriber_zero_cost():
    assert ride_cost("standard", 30, True, False) == 0


def test_subscriber_positive_cost():
    assert ride_cost("standard", 60, True, False) == 20


def test_non_subscriber():
    assert ride_cost("electric", 30, False, False) == 35


def test_peak_non_cargo():
    assert ride_cost("standard", 30, False, True) == 35


def test_peak_cargo():
    assert ride_cost("cargo", 30, False, True) == 50


def test_non_peak_ride():
    assert ride_cost("electric", 30, False, False) == 35


def test_long_ride():
    assert ride_cost("standard", 181, False, False) == 240


def test_exactly_180_minutes():
    assert ride_cost("standard", 180, False, False) == 120


# ---------------- DOCK STATUS ----------------

def test_invalid_capacity():
    with pytest.raises(ValueError):
        dock_status(0, 0)


def test_negative_capacity():
    with pytest.raises(ValueError):
        dock_status(0, -5)


def test_negative_bike_count():
    with pytest.raises(ValueError):
        dock_status(-1, 10)


def test_bikes_exceed_capacity():
    with pytest.raises(ValueError):
        dock_status(11, 10)


def test_empty_dock():
    assert dock_status(0, 10) == "empty"


def test_full_dock():
    assert dock_status(10, 10) == "full"


def test_few_bikes():
    assert dock_status(2, 10) == "few bikes"


def test_available_dock():
    assert dock_status(5, 10) == "available"


def test_few_slots():
    assert dock_status(8, 10) == "few slots"


# ---------------- CAN UNLOCK ----------------

def test_active_ride():
    assert can_unlock(500, True, 25) is False


def test_age_below_16():
    assert can_unlock(500, False, 15) is False


def test_age_16_with_sufficient_balance():
    assert can_unlock(100, False, 16) is True


def test_age_17_with_insufficient_balance():
    assert can_unlock(99, False, 17) is False


def test_age_17_with_exact_balance():
    assert can_unlock(100, False, 17) is True


def test_age_18_with_sufficient_balance():
    assert can_unlock(50, False, 18) is True


def test_adult_with_insufficient_balance():
    assert can_unlock(49, False, 18) is False
