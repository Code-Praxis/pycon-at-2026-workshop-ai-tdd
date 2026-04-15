from typing import NewType

WeightInKg = NewType("WeightInKg", float)
CostsInEuro = NewType("CostsInEuro", float)

BASE_SHIPPING_RATE = 5.0
LOW_TIER_COSTS_PER_KG = 1.0

def calculate_shipping_costs(weight: WeightInKg) -> CostsInEuro:
    return BASE_SHIPPING_RATE + CostsInEuro(weight)*LOW_TIER_COSTS_PER_KG
