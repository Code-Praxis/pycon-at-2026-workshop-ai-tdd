
BASE_SHIPPING_RATE = 5.0
LOW_TIER_COSTS = 1.0

def calculate_shipping_costs(weight: float) -> float:
    return BASE_SHIPPING_RATE + weight*LOW_TIER_COSTS
