"""
Unit tests for calculate_weight_cost.

These tests are WHITE-BOX: they import and call calculate_weight_cost directly.
They are COUPLED to the internal implementation.

Workshop teaching point: these tests will BREAK if you rename calculate_weight_cost
or inline its logic into calculate_delivery_fee. That breakage is intentional —
it demonstrates why tests written against internals are fragile.

Compare with tests/acceptance/test_shipping_costs.py, which survives the same refactor.
"""

from shipping_costs import calculate_weight_cost


class TestTier1:
    """0 to 5 kg @ €1.00/kg"""

    def test_zero_kg(self) -> None:
        assert calculate_weight_cost(0.0) == 0.00

    def test_one_kg(self) -> None:
        assert calculate_weight_cost(1.0) == 1.00

    def test_three_kg(self) -> None:
        assert calculate_weight_cost(3.0) == 3.00

    def test_exactly_five_kg(self) -> None:
        assert calculate_weight_cost(5.0) == 5.00


class TestTier2:
    """5 to 20 kg: first 5 kg @ €1.00, remainder @ €1.50/kg"""

    def test_six_kg(self) -> None:
        # 5×1.00 + 1×1.50 = 6.50
        assert calculate_weight_cost(6.0) == 6.50

    def test_ten_kg(self) -> None:
        # 5×1.00 + 5×1.50 = 12.50
        assert calculate_weight_cost(10.0) == 12.50

    def test_exactly_twenty_kg(self) -> None:
        # 5×1.00 + 15×1.50 = 27.50
        assert calculate_weight_cost(20.0) == 27.50


class TestTier3:
    """Above 20 kg: first 5@€1.00, next 15@€1.50, remainder @ €2.00/kg"""

    def test_twenty_one_kg(self) -> None:
        # 5×1.00 + 15×1.50 + 1×2.00 = 29.50
        assert calculate_weight_cost(21.0) == 29.50

    def test_twenty_five_kg(self) -> None:
        # 5×1.00 + 15×1.50 + 5×2.00 = 37.50
        assert calculate_weight_cost(25.0) == 37.50

    def test_one_hundred_kg(self) -> None:
        # 5×1.00 + 15×1.50 + 80×2.00 = 187.50
        assert calculate_weight_cost(100.0) == 187.50
