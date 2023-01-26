import pyrebase
print("    /\\")
print("   /  \\")
print("  /----\\     Finance Track")
print(" /      \\")
print("/        \\")

print("Welcome to Finance Track by Aryaman!")

config = {
  "apiKey": "AIzaSyDQyY4u2jYns9rY6QiYJOZirUFZUbvy4XE",
  "authDomain": "financetrack-3279c.firebaseapp.com",
  "databaseURL": "https://financetrack-3279c.firebaseapp.com",
  "storageBucket": "financetrack-3279c.appspot.com"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

def add_expense(description, amount):
    expense = {"description": description, "amount": amount}
    db.child("expenses").push(expense)

def view_expenses():
    total_expenses = 0
    expenses = db.child("expenses").get()
    for expense in expenses.each():
        print(expense.val())
        total_expenses += expense.val()['amount']
    print("Total Expenses: $" + str(total_expenses))

def add_income(description, amount):
    income = {"description": description, "amount": amount}
    db.child("income").push(income)

def view_income():
    total_income = 0
    income = db.child("income").get()
    for inc in income.each():
        print(inc.val())
        total_income += inc.val()['amount']
    print("Total Income: $" + str(total_income))

def view_balance():
    expenses = db.child("expenses").get()
    total_expenses = 0
    for expense in expenses.each():
        total_expenses += expense.val()['amount']
    income = db.child("income").get()
    total_income = 0
    for inc in income.each():
        total_income += inc.val()['amount']
    balance = total_income - total_expenses
    print("Balance: $" + str(balance))


view_expenses()
view_income()
view_balance()