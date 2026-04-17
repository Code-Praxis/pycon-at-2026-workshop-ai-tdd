from dataclasses import dataclass
from enum import Enum


class Zone(Enum):
    A = "A"
    B = "B"
    C = "C"


_ZONE_MULTIPLIERS = {
    Zone.A: 1.0,
    Zone.B: 1.5,
    Zone.C: 2.5,
}

BASE_RATE = 5.00
EXPRESS_SURCHARGE = 15.00
MAX_WEIGHT = 100.0


def calculate_weight_cost(weight_kg: float) -> float:
    if weight_kg <= 5:
        return weight_kg * 1.00
    elif weight_kg <= 20:
        return 5 * 1.00 + (weight_kg - 5) * 1.50
    else:
        return 5 * 1.00 + 15 * 1.50 + (weight_kg - 20) * 2.00


def calculate_delivery_fee(weight_kg: float, zone: Zone, express: bool = False) -> float:
    if weight_kg < 0:
        raise ValueError("Weight cannot be negative.")
    if weight_kg > MAX_WEIGHT:
        raise ValueError(f"Weight exceeds maximum allowed ({MAX_WEIGHT} kg).")

    multiplier = _ZONE_MULTIPLIERS[zone]
    fee = (BASE_RATE + calculate_weight_cost(weight_kg)) * multiplier

    if express:
        fee += EXPRESS_SURCHARGE

    return round(fee, 2)


def calculate_shipping_costs(weight: float) -> float:
    @dataclass
    class WeightTier:
        min_weight: float
        multiplier: float

    weight_costs_per_tier = [
        WeightTier(min_weight=20, multiplier=2),
        WeightTier(min_weight=5, multiplier=1.5),
        WeightTier(min_weight=0, multiplier=1),
    ]

    costs = 0
    for weight_tier in weight_costs_per_tier:
        if weight >= weight_tier.min_weight:
            current_tier_weight = weight - weight_tier.min_weight
            costs += current_tier_weight * weight_tier.multiplier
            weight = weight_tier.min_weight

    return costs + BASE_RATE
