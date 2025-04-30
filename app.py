from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    suggested_budget = {}
    if request.method == 'POST':
        income = float(request.form['income'])
        suggested_budget = {
            'Needs (50%)': income * 0.50,
            'Wants (30%)': income * 0.30,
            'Savings (20%)': income * 0.20
        }
    return render_template('index.html', suggested_budget=suggested_budget)

if __name__ == '__main__':
    app.run(debug=True)
