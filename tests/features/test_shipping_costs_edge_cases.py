import pytest

from shipping_costs.calculator import (
    ShippingZone,
    WeightInKg,
    calculate_shipping_costs,
)


def test_negative_weight_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_shipping_costs(weight=WeightInKg(-1.0))


def test_shipping_costs_rounding() -> None:
    # 5.0 base + 0.33333 * 1.0 (Tier 1) = 5.33333
    # Expected rounded to 2 decimals: 5.33
    weight = WeightInKg(0.3333333333333333)
    assert calculate_shipping_costs(weight=weight) == 5.33


def test_shipping_costs_rounding_zones() -> None:
    # 10kg Local: 17.5
    # 10kg Domestic (1.5x): 26.25
    # Let's find a weight that results in more than 2 decimal places after multiplier
    # base 5.0 + 0.01 * 1.0 = 5.01
    # 5.01 * 1.5 = 7.515
    # Python round(7.515, 2) is 7.51 because it rounds to the nearest even number
    # (7.52 if it was 7.525). Actually round(7.515, 2) == 7.51
    weight = WeightInKg(0.01)
    cost = calculate_shipping_costs(weight=weight, zone=ShippingZone.Domestic)
    assert cost == 7.51


def test_extremely_large_weight() -> None:
    # Just to ensure it doesn't crash
    weight = WeightInKg(1e12)
    cost = calculate_shipping_costs(weight=weight)
    assert isinstance(cost, float)
    assert cost > 0
