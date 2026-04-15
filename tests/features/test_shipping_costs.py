import pytest

from shipping_costs.calculator import calculate_shipping_costs, BASE_SHIPPING_RATE


def test_shipping_of_an_empty_order_costs_the_base_rate() -> None:
    assert calculate_shipping_costs(weight=0) == BASE_SHIPPING_RATE

