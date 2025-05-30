def allocate_budget(income):
    allocations = {
        "Needs": round(income * 0.50, 2),
        "Wants": round(income * 0.30, 2),
        "Savings": round(income * 0.20, 2)
    }
    return allocations
