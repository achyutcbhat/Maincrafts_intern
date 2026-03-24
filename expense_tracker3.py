import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create file if not exists
def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass


# Add Expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')

    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    description = input("Enter description: ")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("✅ Expense added successfully!\n")


# View All Expenses
def view_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---")
            for row in reader:
                print(row)
            print()
    except FileNotFoundError:
        print("No data found.\n")


# Search by Category
def search_category():
    search = input("Enter category to search: ").lower()
    found = False

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        print(f"\n--- Expenses in {search} ---")

        for row in reader:
            if row["Category"].lower() == search:
                print(row)
                found = True

    if not found:
        print("No matching records found.\n")
    else:
        print()


# Monthly Total
def monthly_total():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])

    print(f"💰 Total spending for {month}: {total}\n")


# Main Menu
def menu():
    initialize_file()

    while True:
        print("""
----- Expense Tracker -----
1. Add Expense
2. View All Expenses
3. Search by Category
4. Monthly Total
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_category()
        elif choice == '4':
            monthly_total()
        elif choice == '5':
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
menu()
