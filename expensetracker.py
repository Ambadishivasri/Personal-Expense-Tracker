import json
from datetime import datetime

# Function to add an expense
def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    print("Expense added successfully!")

# Function to view summary
def view_summary(expenses):
    category_summary = {}
    total_spending = 0
    for expense in expenses:
        total_spending += expense["amount"]
        if expense["category"] in category_summary:
            category_summary[expense["category"]] += expense["amount"]
        else:
            category_summary[expense["category"]] = expense["amount"]
    
    print("\nTotal Spending by Category:")
    for category, amount in category_summary.items():
        print(f"{category}: ${amount:.2f}")
    print(f"\nTotal Overall Spending: ${total_spending:.2f}")

# Function to save expenses to a file
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved to file.")

# Function to load expenses from a file
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
        print("Expenses loaded from file.")
    except FileNotFoundError:
        expenses = []
        print("No previous expense records found.")
    return expenses

# Main menu function
def main():
    expenses = load_expenses()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add an expense")
        print("2. View summaries")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            save_expenses(expenses)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
