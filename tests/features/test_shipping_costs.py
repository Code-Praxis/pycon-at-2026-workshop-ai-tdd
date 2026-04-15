import pytest

from shipping_costs.calculator import calculate_shipping_costs, BASE_SHIPPING_RATE, WeightInKg, ShippingZone


def test_shipping_of_an_empty_order_costs_the_base_rate() -> None:
    assert calculate_shipping_costs(weight=WeightInKg(0)) == BASE_SHIPPING_RATE


@pytest.mark.parametrize("weight", [WeightInKg(1), WeightInKg(3), WeightInKg(4.99)])
def test_shipping_costs_for_low_weight_tiers(weight: WeightInKg) -> None:
    # 5.0 base + 1.0 per kg for first tier
    assert calculate_shipping_costs(weight=weight) == 5.0 + float(weight) * 1.0


@pytest.mark.parametrize("weight", [WeightInKg(5), WeightInKg(10), WeightInKg(20)])
def test_shipping_costs_for_medium_weight_tiers(weight: WeightInKg) -> None:
    expected_cost = 10.0 + (float(weight) - 5.0) * 1.5
    assert calculate_shipping_costs(weight=weight) == expected_cost


@pytest.mark.parametrize("weight", [WeightInKg(21), WeightInKg(30)])
def test_shipping_costs_for_high_weight_tiers(weight: WeightInKg) -> None:
    # 5.0 base + 5.0 * 1.0 (Tier 1) + 15.0 * 1.5 (Tier 2) + (weight - 20) * 2.0 (Tier 3)
    # 5.0 + 5.0 + 22.5 = 32.5 base for tier 3
    expected_cost = 32.5 + (float(weight) - 20.0) * 2.0
    assert calculate_shipping_costs(weight=weight) == expected_cost


@pytest.mark.parametrize(
    "zone, expected_multiplier",
    [
        (ShippingZone.A, 1.0),
        (ShippingZone.B, 1.5),
        (ShippingZone.C, 2.5),
    ],
)
def test_shipping_costs_for_different_zones(zone: ShippingZone, expected_multiplier: float) -> None:
    weight = WeightInKg(10)
    # Cost for 10kg in Zone A: 5.0 (base) + 5.0*1.0 (Tier 1) + 5.0*1.5 (Tier 2) = 17.5
    base_cost = 17.5
    assert calculate_shipping_costs(weight=weight, zone=zone) == base_cost * expected_multiplier
