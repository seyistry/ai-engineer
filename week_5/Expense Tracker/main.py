# @title 17. Basic Expense Tracker
"""
An Expense Tracker is a practical application that
allows users to log their daily expenses and track spending
habits. This project enhances knowledge of file handling,
data storage, and user input processing in Python.
This chapter covers the step-by-step implementation of an
Expense Tracker, including user input handling, data storage
in a CSV file, and displaying expense reports.

Key Concepts of Expense Tracker in Python

Data Handling:

Using lists and dictionaries to store
expenses
Writing and reading data from a CSV file

User Input Processing:

Taking user input for expense details
Validating and formatting input data

Report Generation:

Displaying total expenses per category
Summarizing daily or monthly spending

"""
import csv
import os
from datetime import datetime

# Load expenses from CSV file
def load_expenses(filename):
    expenses = []
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(row)
    return expenses

# Save expenses to CSV file
def save_expenses(filename, expenses):
    with open(filename, 'w', newline='') as f:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

# Add a new expense
def add_expense(expenses):
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return
    category = input("Enter category: ").strip()
    amount_str = input("Enter amount: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount.")
        return
    expenses.append(
        {'date': date_str, 'category': category, 'amount': str(amount)})
    print("Expense added.")

# Display all expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['date']} | {exp['category']} | ₦{exp['amount']}")

# Report: total per category
def report_by_category(expenses):
    totals = {}
    for exp in expenses:
        cat = exp['category']
        amt = float(exp['amount'])
        totals[cat] = totals.get(cat, 0) + amt
    print("\nTotal Expenses by Category:")
    for cat, total in totals.items():
        print(f"{cat}: ₦{total:.2f}")

# Report: total per month
def report_by_month(expenses):
    monthly = {}
    for exp in expenses:
        month = exp['date'][:7]  # YYYY-MM
        amt = float(exp['amount'])
        monthly[month] = monthly.get(month, 0) + amt
    print("\nTotal Expenses by Month:")
    for month, total in monthly.items():
        print(f"{month}: ₦{total:.2f}")

# Main loop
def main():
    filename = "expenses.csv"
    expenses = load_expenses(filename)
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Report by Category")
        print("4. Report by Month")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(filename, expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            report_by_category(expenses)
        elif choice == "4":
            report_by_month(expenses)
        elif choice == "5":
            save_expenses(filename, expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
