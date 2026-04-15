import pytest

from shipping_costs.calculator import calculate_shipping_costs, BASE_SHIPPING_RATE, LOW_TIER_COSTS_PER_KG, WeightInKg


def test_shipping_of_an_empty_order_costs_the_base_rate() -> None:
    assert calculate_shipping_costs(weight=0) == BASE_SHIPPING_RATE


@pytest.mark.parametrize("weight", [1, 3, 4.99])
def test_shipping_costs_for_low_weight_tiers(weight: WeightInKg) -> None:
    assert calculate_shipping_costs(weight=weight) == BASE_SHIPPING_RATE + float(weight) * LOW_TIER_COSTS_PER_KG