import pytest

from shipping_costs.calculator import calculate_shipping_costs, BASE_SHIPPING_RATE, LOW_TIER_COSTS


def test_shipping_of_an_empty_order_costs_the_base_rate() -> None:
    assert calculate_shipping_costs(weight=0) == BASE_SHIPPING_RATE


def test_when_shipping_less_than_five_kg_it_costs_increased_rate() -> None:
    assert calculate_shipping_costs(weight=3) == BASE_SHIPPING_RATE + 3.0*LOW_TIER_COSTS