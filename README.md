
---

#  Budget Planning System

##  Objective

Provide personalized monthly budget suggestions based on a user's income and expenses using proportional allocation and rule-based financial guidance.

---

##  Computational Techniques

1. **Proportional Allocation** – Uses budgeting rules such as 50/30/20 and 60/10/10/10/10 to distribute income across essential categories.
2. **Rule-Based Guidance** – Provides spending, savings, and debt-reduction advice based on established financial guidelines.

---

## 🖥️ User Interface (Flask + Bootstrap + Chart.js)

* Input fields for total monthly income and expenses
* Interactive pie chart for budget visualization
* Breakdown of allocations vs. benchmark data
* Rule-based financial advice and category-specific tips

---

##  Types of Datasets Used

1. **Household Spending Patterns** – For benchmarking allocations by income bracket
2. **Financial Planning Guidelines** – For rule-based advice and savings/debt strategies

---

## 🔗 Dataset Sources

* [BLS Consumer Expenditure Surveys (CEX)](https://www.bls.gov/cex/pumd_data.htm)
* [Consumer Financial Protection Bureau Research](https://www.consumerfinance.gov/data-research/)

---

##  Setup Instructions

### Step-by-step Guide:

1. Clone the repository:

   ```bash
   git clone https://github.com/imosudi/Budget-Planning-System.git
   cd Budget-Planning-System
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   flask run
   ```

---

##  Features Implemented

*  Flask app with income and expense input
*  Budget allocation using 50/30/20 or extended rules
*  Dynamic category amount calculation
*  Overspending rebalancing logic
*  Interactive pie chart (Chart.js)
*  Financial advice with rule-based logic
*  Benchmark database for income-specific guidance
*  Comparison against ideal financial ratios
*  Testing across financial profiles (ongoing/expandable)

---

##  Future Enhancements

*  Add support for multiple currencies
*  Expand advice using user financial goals
*  Integrate lightweight ML model to adapt advice over time
*  Add unit and functional tests across diverse income scenarios

---

##  Feedback / Contributions

Have a suggestion, or want to contribute? Feel free to fork this project and submit a pull request!

