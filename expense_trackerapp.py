import sqlite3
import argparse
import logging
from datetime import datetime

# ----------------- Logging Setup -----------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------- Database Setup -----------------
def connect_db():
    return sqlite3.connect("expenses.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

# ----------------- Add Expense -----------------
def add_expense(amount, category, description):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        category = category.title()  # Normalize

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses (amount, category, date, description)
            VALUES (?, ?, ?, ?)
        """, (amount, category, datetime.now().strftime("%Y-%m-%d"), description))

        conn.commit()
        conn.close()

        print("✅ Expense added successfully!")
        logging.info(f"Added expense: {amount}, {category}")

    except Exception as e:
        print("❌ Error adding expense:", e)
        logging.error(str(e))

# ----------------- List Expenses -----------------
def list_expenses():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")

        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("No expenses found.")
            return

        print("\n--- Expenses ---")
        for row in rows:
            print(row)

        logging.info("Listed expenses")

    except Exception as e:
        print("❌ Error listing expenses:", e)
        logging.error(str(e))

# ----------------- Delete Expense -----------------
def delete_expense(expense_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        conn.commit()
        conn.close()

        print("🗑️ Expense deleted!")
        logging.info(f"Deleted expense ID: {expense_id}")

    except Exception as e:
        print("❌ Error deleting expense:", e)
        logging.error(str(e))

# ----------------- Report -----------------
def report(month=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        if month:
            cursor.execute("""
                SELECT category, SUM(amount)
                FROM expenses
                WHERE strftime('%Y-%m', date) = ?
                GROUP BY category
            """, (month,))
        else:
            cursor.execute("""
                SELECT category, SUM(amount)
                FROM expenses
                GROUP BY category
            """)

        rows = cursor.fetchall()
        conn.close()

        print("\n--- Report ---")
        for row in rows:
            print(f"{row[0]}: {row[1]}")

        logging.info("Generated report")

    except Exception as e:
        print("❌ Error generating report:", e)
        logging.error(str(e))

# ----------------- CLI Setup -----------------
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    subparsers = parser.add_subparsers(dest="command")

    # Add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--amount", required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--desc", default="")

    # List
    subparsers.add_parser("list")

    # Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True)

    # Report
    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("--month", help="Format: YYYY-MM")

    args = parser.parse_args()

    create_table()

    if args.command == "add":
        add_expense(args.amount, args.category, args.desc)

    elif args.command == "list":
        list_expenses()

    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == "report":
        report(args.month)

    else:
        parser.print_help()

# ----------------- Run -----------------
if __name__ == "__main__":
    main()
