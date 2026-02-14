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
add_expense()
