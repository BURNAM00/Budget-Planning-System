def generate_advice(income, expenses, allocations):
    advice = []

    # Check if expenses are more than income
    if expenses > income:
        advice.append("Your expenses exceed your income. Consider cutting back on spending.")

    # Check if needs exceed 50%
    # (Assuming user provides actual 'needs' spending; else use expenses for demo)
    # For now, just an example comparing total expenses to recommended 'needs' allocation
    if expenses > allocations["Needs"]:
        advice.append("You are spending more than recommended on essential needs. Try to reduce these costs.")

    # Check savings
    recommended_savings = allocations["Savings"]
    # Assume savings = income - expenses 
    actual_savings = income - expenses
    if actual_savings < recommended_savings:
        advice.append("Your savings are below the recommended 20%. Try to save more each month.")

    # General advice
    if income < 1000:
        advice.append("Your income is quite low, consider finding ways to increase your income or reduce expenses.")

    if not advice:
        advice.append("Your budget looks good! Keep up the good work.")

    return advice
