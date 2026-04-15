from dataclasses import dataclass
from enum import StrEnum, auto
from typing import NewType

WeightInKg = NewType("WeightInKg", float)
CostsInEuro = NewType("CostsInEuro", float)


class ShippingZone(StrEnum):
    Local = auto()
    Domestic = auto()
    International = auto()


ZONE_MULTIPLIERS = {
    ShippingZone.Local: 1.0,
    ShippingZone.Domestic: 1.5,
    ShippingZone.International: 2.5,
}


@dataclass(frozen=True)
class ShippingTier:
    max_weight: float
    rate_per_kg: float


BASE_SHIPPING_RATE = 5.0
EXPRESS_SURCHARGE = 15.0

TIERS = [
    ShippingTier(max_weight=5.0, rate_per_kg=1.0),
    ShippingTier(max_weight=20.0, rate_per_kg=1.5),
    ShippingTier(max_weight=float("inf"), rate_per_kg=2.0),
]


def calculate_shipping_costs(
    weight: WeightInKg, zone: ShippingZone = ShippingZone.Local, is_express: bool = False
) -> CostsInEuro:
    if float(weight) < 0:
        raise ValueError("Weight cannot be negative")

    remaining_weight = float(weight)
    total_cost = BASE_SHIPPING_RATE

    previous_max_weight = 0.0
    for tier in TIERS:
        weight_in_tier = min(remaining_weight, tier.max_weight - previous_max_weight)
        if weight_in_tier <= 0:
            break

        total_cost += weight_in_tier * tier.rate_per_kg
        remaining_weight -= weight_in_tier
        previous_max_weight = tier.max_weight

    multiplier = ZONE_MULTIPLIERS[zone]
    final_cost = total_cost * multiplier

    if is_express:
        final_cost += EXPRESS_SURCHARGE

    return CostsInEuro(round(final_cost, 2))
