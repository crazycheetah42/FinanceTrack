import os

# Function to add an expense
def add_expense(expense_name, expense_amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{expense_name},{expense_amount}\n")
    print(f"Expense {expense_name} of {expense_amount} added.")

# Function to display expenses
def display_expenses():
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
    if not expenses:
        print("No expenses found.")
    else:
        print("Expenses:")
        for expense in expenses:
            expense_name, expense_amount = expense.strip().split(",")
            print(f"{expense_name} - {expense_amount}")

# Function to remove an expense
def remove_expense(expense_name):
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            if expense_name not in expense:
                file.write(expense)
    print(f"Expense {expense_name} removed.")
    
# Function to add an income
def add_income(income_name, income_amount):
    with open("income.txt", "a") as file:
        file.write(f"{income_name},{income_amount}\n")
    print(f"Income {income_name} of {income_amount} added.")

# Function to display income
def display_income():
    with open("income.txt", "r") as file:
        income = file.readlines()
    if not income:
        print("No income found.")
    else:
        print("Income:")
        for inc in income:
            income_name, income_amount = inc.strip().split(",")
            print(f"{income_name} - {income_amount}")

while True:
    print("    /\\")
    print("   /  \\")
    print("  /----\\     Finance Tracker")
    print(" /      \\")
    print("/        \\")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Expenses")
    print("4. View Income")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        expense_name = input("Enter expense name: ")
        expense_amount = input("Enter expense amount: ")
        add_expense(expense_name, float(expense_amount))
    elif choice == '2':
        income_name = input("Enter income name: ")
        income_amount = input("Enter income amount: ")
        add_income(income_name, float(income_amount))
    elif choice == '3':
        print(display_expenses())
    elif choice == '4':
        print(display_income())
    elif choice == '5':
        print("Exiting the app...")
        break
    else:
        print("Invalid choice. Please try again.")