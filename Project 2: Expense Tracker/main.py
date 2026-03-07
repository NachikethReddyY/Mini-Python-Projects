"""
**Simple Expense Tracker**
- **Need:** Keep track of personal income and expenses.
- **Modules Needed:** `json`, `csv`, `datetime`
- **Description:** A program to log expenses, categorize them, and display simple reports (e.g., total by category).
- **Challenges:** Data aggregation, CSV/json formatting, user input validation.

| Expense Name | Amount | Category | date |
| ------------ | ------ | -------- | ---- |
|              |        |          |      |
Menu:
1. Log an expense
2. View Category Expenses (Second Menu)
3. View Month's Expenses (Second Menu)`
4. Save and Exit.
"""

import csv
import datetime
import os


class Expense:
        def __init__(self, expense_name, expense_amount, expense_category):
                self.amount = expense_amount
                self.date = datetime.date.today()
                self.name = expense_name
                self.category = expense_category
        def display(self):
                print(f"  {self.date.strftime('%Y-%m-%d')}  │  {self.name:<18}  │  ${self.amount:>9.2f}  │  {self.category:<12}")

class ExpenseManager:
        def __init__(self):
                self.expenses = []
        def add_expense(self, expense_name, expense_amount, expense_category):
                expense = Expense(expense_name, expense_amount, expense_category)
                self.expenses.append(expense)
        def view_expenses_month(self):
                # Step 1: Get unique month-year combinations
                months = []
                month_data = []
                for expense in self.expenses:
                        # month_year = expense.date.strftime("%B %Y")  # "March 2026"
                        # if month_year not in months:
                        #         months.append(month_year)
                        year = expense.date.year
                        month_num = expense.date.month
                        month_string = expense.date.strftime("%B %Y")  # "March 2026"
                        if (year, month_num, month_string) not in month_data:
                                month_data.append((year, month_num, month_string))

                # Step 2: Sort and extract display strings
                month_data = sorted(month_data, reverse=True)
                months = [m[2] for m in month_data]

                # Step 3: Show menu
                print("\nAvailable Months:")
                for i, month in enumerate(months, 1):
                        print(f"{i}. {month}")

                # Step 4: Get selection
                choice = int(input("Select month: ")) - 1
                selected = months[choice]  # e.g., "March 2026"

                # Step 5: Parse the selected month-year back to compare
                # Split "March 2026" into month name and year
                month_name, year = selected.split()  # ["March", "2026"]
                month_num = datetime.datetime.strptime(month_name, "%B").month  # 3

                # Step 6: Filter and show
                print(f"\n  {'Date':<10}  │  {'Name':<18}  │  {'Amount':>10}  │  {'Category':<12}")
                print("  " + "─" * 74)
                total = 0
                for expense in self.expenses:
                        if expense.date.month == month_num and expense.date.year == int(year):
                                expense.display()
                                total += expense.amount
                print("  " + "─" * 74)
                print(f"  {'TOTAL':<31}  │  ${total:>9.2f}")

        def view_expenses_category(self):
                # Step 1: Get unique categories
                categories = []
                for expense in self.expenses:
                        if expense.category not in categories:
                                categories.append(expense.category)
                categories = sorted(categories)

                # Step 2: Show menu
                print("\nAvailable Categories:")
                for i, category in enumerate(categories, 1):
                        print(f"{i}. {category}")

                # Step 3: Get selection
                choice = int(input("Select category: ")) - 1
                selected = categories[choice]

                # Step 4: Filter and show
                print(f"\n  {'Date':<10}  │  {'Name':<18}  │  {'Amount':>10}  │  {'Category':<12}")
                print("  " + "─" * 74)
                total = 0
                for expense in self.expenses:
                        if expense.category == selected:
                                expense.display()
                                total += expense.amount
                print("  " + "─" * 74)
                print(f"  {'TOTAL':<31}  │  ${total:>9.2f}")
        def save_to_file(self, filename="report.csv"):
                with open(filename, "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(["Date", "Name", "Amount", "Category"])
                        for expense in self.expenses:
                                writer.writerow([expense.date.strftime("%Y-%m-%d"), expense.name, expense.amount, expense.category])
        def load_from_file(self, filename="report.csv"):
                if not os.path.isfile(filename):
                        return
                with open(filename, "r", newline="") as file:
                        data = csv.reader(file)
                        self.expenses = []
                        next(data) #skip header row
                        for row in data:
                                expense = Expense(row[1], float(row[2]), row[3])
                                expense.date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
                                self.expenses.append(expense)






def main():
    manager = ExpenseManager()
    manager.load_from_file()

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          💰  WELCOME TO EXPENSE MANAGER  💰              ║
║                                                          ║
║         Track your expenses with Python!                 ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    while True:
        print("""
┌────────────────────────────────────┐
│         SERVICES AVAILABLE         │
├────────────────────────────────────┤
│  1. Log an expense                 │
│  2. View Category Expenses         │
│  3. View Month's Expenses          │
│  4. Save and Exit                  │
└────────────────────────────────────┘""")

        service = input("\n  Enter your choice (1-4): ")

        if service == "1":
            print("\n  ──────────────────────────────────────")
            print("         ADD NEW EXPENSE")
            print("  ──────────────────────────────────────")
            name = input("  Enter expense name: ")
            amount = float(input("  Enter amount: $"))
            category = input("  Enter category: ")
            manager.add_expense(name, amount, category)
            print(f"\n  ✅ Expense added: {name} - ${amount:.2f} ({category})")
            input("\n  Press Enter to continue...")

        elif service == "2":
            manager.view_expenses_category()
            input("\n  Press Enter to continue...")

        elif service == "3":
            manager.view_expenses_month()
            input("\n  Press Enter to continue...")

        elif service == "4":
            manager.save_to_file()
            print("\n  ✅ Expenses saved to report.csv")
            print("  Goodbye! 👋\n")
            break

        else:
            print("\n  ❌ Invalid choice. Please enter 1-4.")
            input("  Press Enter to continue...")


if __name__ == "__main__":
    main()
