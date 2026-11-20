
import csv
import os

FILE = "expenses.csv"


# Add Expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Description"])

        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# View Expenses
def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses found!")
        return

    with open(FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


# Filter Expenses
def filter_expenses():
    category = input("Enter category to filter: ").lower()

    if not os.path.exists(FILE):
        print("No expenses found!")
        return

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].lower() == category:
                print(row)


# Category Summary
def summary():
    totals = {}

    if not os.path.exists(FILE):
        print("No expenses found!")
        return

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    print("\n===== EXPENSE SUMMARY =====")

    for category, amount in totals.items():
        print(category, ":", amount)

    print("Total Expenses:", sum(totals.values()))


# Main Menu
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        summary()
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Try again.")
