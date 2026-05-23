from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

# create file if not exists
if not os.path.exists("expenses.txt"):
    open("expenses.txt", "w").close()


# 🟢 HOME
@app.route('/')
def home():
    return render_template("index.html")


# 🟢 ADD EXPENSE
@app.route('/add', methods=['POST'])
def add():
    amount = request.form['amount']
    category = request.form['category']
    note = request.form['note']

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("expenses.txt", "a") as file:
        file.write(f"{timestamp},{amount},{category},{note}\n")

    return "<h3>✅ Expense Added!</h3><a href='/'>Add More</a> | <a href='/view'>View Expenses</a>"


# 🟢 VIEW ALL EXPENSES
@app.route('/view')
def view():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                timestamp, amount, category, note = line.strip().split(",")
                expenses.append({
                    "timestamp": timestamp,
                    "amount": amount,
                    "category": category,
                    "note": note
                })
    except:
        pass

    return render_template("view.html", expenses=expenses)


# 🟢 TOTAL EXPENSE
@app.route('/total')
def total():
    total_amount = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                _, amount, _, _ = line.strip().split(",")
                total_amount += float(amount)
    except:
        pass

    return f"<h2>Total Expense: {total_amount}</h2><a href='/'>Go Back</a>"


# 🟢 CATEGORY FILTER
@app.route('/category', methods=['GET', 'POST'])
def category():
    expenses = []

    if request.method == 'POST':
        selected_category = request.form['category']

        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    timestamp, amount, category, note = line.strip().split(",")

                    if category.lower() == selected_category.lower():
                        expenses.append({
                            "timestamp": timestamp,
                            "amount": amount,
                            "category": category,
                            "note": note
                        })
        except:
            pass

    return render_template("category.html", expenses=expenses)


# 🟢 CLEAR ALL
@app.route('/clear')
def clear():
    open("expenses.txt", "w").close()
    return "<h3>All expenses cleared ❌</h3><a href='/'>Go Back</a>"


# 🟢 RUN APP
if __name__ == '__main__':
    app.run(debug=True)
