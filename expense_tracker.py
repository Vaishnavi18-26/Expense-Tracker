from datetime import datetime
import os

# create file if it does not exist
if not os.path.exists("expenses.txt"):
    open("expenses.txt", "w").close()


def print_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Total")
    print("5. Clear All Expenses")
    print("6. Exit")


def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ")
    note = input("Enter note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category},{note}\n")

    print("Expense added successfully!")


def view_expenses():
    print("\n----- Expense List -----")

    try:
        with open("expenses.txt", "r") as file:
            print("Amount | Category | Note")
            print("------------------------")

            for line in file:
                amount, category, note = line.strip().split(",")
                timestamp, amount, category, note = line.strip().split(",")
                print(f"{amount} | {category} | {note}")

    except FileNotFoundError:
        print("No expenses found.")


def total_expense():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, _, _ = line.strip().split(",")
                total += float(amount)

        print("Total Expense:", total)

    except FileNotFoundError:
        print("No expenses found.")


def category_total():
    category_input = input("Enter category: ")
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category, _ = line.strip().split(",")

                if category.lower() == category_input.lower():
                    total += float(amount)

        print(f"Total expense for {category_input}: {total}")

    except FileNotFoundError:
        print("No expenses found.")


def clear_expenses():
    confirm = input("Are you sure you want to delete all expenses? (yes/no): ")

    if confirm.lower() == "yes":
        open("expenses.txt", "w").close()
        print("All expenses cleared.")
    else:
        print("Operation cancelled.")


# -------- Main Menu --------
while True:

    print_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        category_total()

    elif choice == "5":
        clear_expenses()

    elif choice == "6":
        print("Exiting Expense Tracker")
        break

    else:
        print("Invalid choice")
