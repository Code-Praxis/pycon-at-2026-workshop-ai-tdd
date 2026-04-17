from shipping_costs import Zone, calculate_delivery_fee

if __name__ == "__main__":
    examples = [
        (3.0, Zone.A, False),
        (10.0, Zone.B, False),
        (25.0, Zone.C, True),
    ]
    for weight, zone, express in examples:
        fee = calculate_delivery_fee(weight, zone, express)
        print(f"Weight: {weight} kg, Zone: {zone.value}, Express: {express} → {fee:.2f} €")
