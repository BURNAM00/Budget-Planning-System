BENCHMARKS = {
    (0, 2000): {"Needs": 0.55, "Wants": 0.25, "Savings": 0.20},
    (2001, 5000): {"Needs": 0.50, "Wants": 0.30, "Savings": 0.20},
    (5001, 10000): {"Needs": 0.45, "Wants": 0.35, "Savings": 0.20},
    (10001, 1000000): {"Needs": 0.40, "Wants": 0.40, "Savings": 0.20}
}


def get_benchmark(income):
    for income_range, allocation in BENCHMARKS.items():
        low, high = income_range
        if low <= income <= high:
            return allocation
    # Default fallback
    return {"Needs": 0.50, "Wants": 0.30, "Savings": 0.20}

