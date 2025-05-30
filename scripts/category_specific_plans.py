def category_specific_plans(allocations):
    plans = {}

    if allocations["Needs"] > 0:
        plans["Needs"] = "Try to limit essential expenses to 50% of your income. Consider negotiating bills or finding cheaper alternatives."

    if allocations["Wants"] > 0:
        plans["Wants"] = "Keep discretionary spending within 30%. Prioritize important wants and avoid impulse purchases."

    if allocations["Savings"] > 0:
        plans["Savings"] = "Aim to save at least 20%. Set up automatic transfers to your savings account to build an emergency fund."

    return plans
