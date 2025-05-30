from flask import render_template, request
from scripts.budget_allocate import allocate_budget 
from scripts.generate_advice import generate_advice
from scripts.get_benchmark import get_benchmark
from scripts.category_specific_plans import category_specific_plans
from scripts.compare_with_ideal import compare_with_ideal
from . import app


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    income = float(request.form['income'])
    expenses = float(request.form['expenses'])

    user_allocations = allocate_budget(income)
    benchmark = get_benchmark(income)
    benchmark_dollars = {k: round(v * income, 2) for k, v in benchmark.items()}
    advice = generate_advice(income, expenses, user_allocations)
    plans = category_specific_plans(user_allocations)
    comparison = compare_with_ideal(income, user_allocations)

    return render_template('budget_result.html',
                           income=income,
                           expenses=expenses,
                           allocations=user_allocations,
                           benchmark=benchmark_dollars,
                           advice=advice,
                           plans=plans,
                           comparison=comparison)



if __name__ == '__main__':
    app.run(debug=True)
