IDEAL_RATIOS = {
    "Needs": 0.50,
    "Wants": 0.30,
    "Savings": 0.20
}

def compare_with_ideal(income, allocations):
    comparison = {}
    for category, ideal_pct in IDEAL_RATIOS.items():
        ideal_amount = round(income * ideal_pct, 2)
        actual_amount = allocations.get(category, 0)
        diff = actual_amount - ideal_amount
        if diff > 0:
            comparison[category] = f"You are spending ${diff:.2f} more than ideal on {category}."
        elif diff < 0:
            comparison[category] = f"You are spending ${-diff:.2f} less than ideal on {category}."
        else:
            comparison[category] = f"Your spending on {category} matches the ideal."
    return comparison
