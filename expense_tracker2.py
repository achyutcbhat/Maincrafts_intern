import csv
import os

FILE_NAME = "expenses.csv"

# Add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])

    print("Expense added successfully!\n")


# View all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded.\n")
        return

    print("\nDate | Description | Category | Amount")
    print("--------------------------------------")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()


# Search expenses by category
def search_by_category():
    category_search = input("Enter category to search: ")

    if not os.path.exists(FILE_NAME):
        print("No expenses recorded.\n")
        return

    print("\nMatching Expenses:")
    print("--------------------------------------")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        found = False

        for row in reader:
            if row[2].lower() == category_search.lower():
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
                found = True

        if not found:
            print("No matching expenses found.")

    print()


# Total spent per category
def total_by_category():
    category_search = input("Enter category: ")
    total = 0

    if not os.path.exists(FILE_NAME):
        print("No expenses recorded.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[2].lower() == category_search.lower():
                total += float(row[3])

    print(f"Total spent on {category_search}: {total}\n")


# Monthly spending
def monthly_spending():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    if not os.path.exists(FILE_NAME):
        print("No expenses recorded.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0].startswith(month):
                total += float(row[3])

    print(f"Total spending for {month}: {total}\n")


# Main menu
def main():
    while True:
        print("====== Expense Tracker 2.0 ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Total by Category")
        print("5. Monthly Spending")
        print("6. Exit")

        choice = input("Choose option (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            total_by_category()
        elif choice == "5":
            monthly_spending()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
