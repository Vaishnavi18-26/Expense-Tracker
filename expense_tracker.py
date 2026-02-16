"""
Expense Tracker - Day 1

Features:
- Add a new expense
- Store expense in a file

Each expense is saved as:
amount,category,note
"""

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    note = input("Enter note: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category},{note}\n")

    print("Expense added successfully!")


# Program starts here
# ---------- Day 2 Feature ----------
def view_expenses():
    print("\n--- All Expenses ---")

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category, note = line.strip().split(",")
                print(f"Amount: {amount}, Category: {category}, Note: {note}")
    except FileNotFoundError:
        print("No expenses found.")


# ---------- Main Menu ----------
print("\nExpense Tracker")
print("1. Add Expense")
print("2. View Expenses")

choice = input("Enter your choice: ")

if choice == "1":
    add_expense()
elif choice == "2":
    view_expenses()
else:
    print("Invalid choice")
