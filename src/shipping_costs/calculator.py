from typing import NewType
from dataclasses import dataclass

WeightInKg = NewType("WeightInKg", float)
CostsInEuro = NewType("CostsInEuro", float)

@dataclass(frozen=True)
class ShippingTier:
    max_weight: float
    rate_per_kg: float

BASE_SHIPPING_RATE = 5.0

TIERS = [
    ShippingTier(max_weight=5.0, rate_per_kg=1.0),
    ShippingTier(max_weight=20.0, rate_per_kg=1.5),
    ShippingTier(max_weight=float('inf'), rate_per_kg=2.0),
]

def calculate_shipping_costs(weight: WeightInKg) -> CostsInEuro:
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
        
    return CostsInEuro(total_cost)
