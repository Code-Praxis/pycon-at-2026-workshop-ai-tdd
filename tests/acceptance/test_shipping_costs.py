"""
Acceptance tests for calculate_delivery_fee.

These tests are BLACK-BOX: they call calculate_delivery_fee and assert on the
observable output only. They do NOT import or reference calculate_weight_cost.

Workshop teaching point: these tests survive refactoring the internals.
If you rename calculate_weight_cost or rewrite calculate_shipping_costs,
these tests stay GREEN.
"""

import pytest

from shipping_costs import Zone, calculate_delivery_fee


class TestWeightBasedFee:
    def test_lightweight_package_zone_a(self) -> None:
        assert calculate_delivery_fee(3.0, Zone.A) == 8.00

    def test_package_at_tier1_boundary_zone_a(self) -> None:
        assert calculate_delivery_fee(5.0, Zone.A) == 10.00

    def test_package_crossing_tier1_boundary_zone_a(self) -> None:
        # weight_cost: 5×1.00 + 5×1.50 = 12.50; fee: (5+12.5)×1.0 = 17.50
        assert calculate_delivery_fee(10.0, Zone.A) == 17.50

    def test_package_at_tier2_boundary_zone_a(self) -> None:
        # weight_cost: 5×1.00 + 15×1.50 = 27.50; fee: (5+27.5)×1.0 = 32.50
        assert calculate_delivery_fee(20.0, Zone.A) == 32.50

    def test_heavy_package_zone_a(self) -> None:
        # weight_cost: 5+22.5+10 = 37.50; fee: (5+37.5)×1.0 = 42.50
        assert calculate_delivery_fee(25.0, Zone.A) == 42.50

    def test_zero_weight_zone_a(self) -> None:
        assert calculate_delivery_fee(0.0, Zone.A) == 5.00

    def test_maximum_weight_zone_a(self) -> None:
        # weight_cost: 5+22.5+160 = 187.50; fee: (5+187.5)×1.0 = 192.50
        assert calculate_delivery_fee(100.0, Zone.A) == 192.50


class TestZoneMultiplier:
    def test_zone_b_multiplies_full_subtotal(self) -> None:
        # (BASE_RATE + weight_cost) × 1.5, not BASE_RATE + weight_cost×1.5
        assert calculate_delivery_fee(3.0, Zone.B) == 12.00

    def test_zone_c_multiplies_full_subtotal(self) -> None:
        assert calculate_delivery_fee(3.0, Zone.C) == 20.00

    def test_zone_b_with_multi_tier_weight(self) -> None:
        assert calculate_delivery_fee(10.0, Zone.B) == 26.25

    def test_zone_c_with_multi_tier_weight(self) -> None:
        assert calculate_delivery_fee(10.0, Zone.C) == 43.75


class TestExpressSurcharge:
    def test_express_adds_fifteen_euros(self) -> None:
        assert calculate_delivery_fee(3.0, Zone.A, express=True) == 23.00

    def test_express_false_unchanged(self) -> None:
        assert calculate_delivery_fee(3.0, Zone.A, express=False) == 8.00

    def test_express_applies_after_zone_multiplication(self) -> None:
        # (5+3)×2.5 + 15 = 20+15 = 35, NOT (5+3+15)×2.5
        assert calculate_delivery_fee(3.0, Zone.C, express=True) == 35.00

    def test_express_defaults_to_false(self) -> None:
        without_flag = calculate_delivery_fee(3.0, Zone.A)
        explicit_false = calculate_delivery_fee(3.0, Zone.A, express=False)
        assert without_flag == explicit_false


class TestInputValidation:
    def test_negative_weight_raises_value_error(self) -> None:
        with pytest.raises(ValueError, match="Weight cannot be negative."):
            calculate_delivery_fee(-1.0, Zone.A)

    def test_slightly_negative_weight_raises_value_error(self) -> None:
        with pytest.raises(ValueError, match="Weight cannot be negative."):
            calculate_delivery_fee(-0.001, Zone.A)

    def test_over_maximum_weight_raises_value_error(self) -> None:
        with pytest.raises(ValueError, match="Weight exceeds maximum allowed"):
            calculate_delivery_fee(100.001, Zone.A)

    def test_zero_weight_is_valid(self) -> None:
        result = calculate_delivery_fee(0.0, Zone.A)
        assert isinstance(result, float)
        assert result > 0

    def test_maximum_weight_is_valid(self) -> None:
        result = calculate_delivery_fee(100.0, Zone.A)
        assert isinstance(result, float)
        assert result > 0

    def test_return_type_is_float(self) -> None:
        assert isinstance(calculate_delivery_fee(3.0, Zone.A), float)

    def test_return_is_rounded_to_two_decimal_places(self) -> None:
        result = calculate_delivery_fee(3.0, Zone.A)
        assert result == round(result, 2)
