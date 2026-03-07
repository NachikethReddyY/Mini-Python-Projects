# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python learning project - a command-line Expense Tracker. The user is learning Python fundamentals including classes, file I/O, JSON persistence, CSV export, and program architecture.

**Important Context:**
- This is an educational project - the user is learning Python
- Always use "Learning" output style with "Learn by Doing" sections
- The user writes the code; you provide guidance and review
- Use TODO(human) comments to mark sections for the user to implement
- Wait for user implementation before proceeding to next feature

## Architecture Pattern

This project follows a consistent three-part design:

### 1. Data Class (Expense)
Represents a single expense:
- `__init__(self, name, amount, category)` - stores name, amount, category, timestamp
- `display(self)` - returns formatted string

### 2. Manager Class (ExpenseManager)
Handles collections and persistence:
- `__init__(self)` - Initialize with empty list for expenses
- `add_expense(self, name, amount, category)` - Create Expense and add to list
- `view_expenses(self)` - Loop and display all expenses
- `view_by_category(self)` - Filter and show expenses by category
- `view_by_month(self, month)` - Filter and show expenses by month
- `save_to_file(self)` - Convert objects to dicts, write JSON
- `load_from_file(self)` - Read JSON, recreate objects
- `export_to_csv(self, filename)` - Export expenses to CSV report

### 3. Menu Loop
Console interface with `while True`:
- Display options
- Get user input
- Route to manager methods
- Sub-menus for category/month views
- `break` on exit option

```python
def main():
    manager = ExpenseManager()
    manager.load_from_file()

    while True:
        print("\n1. Add\n2. View\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            # handle add
        elif choice == "2":
            # handle view
        elif choice == "3":
            manager.save_to_file()
            break

if __name__ == "__main__":
    main()
```

## Development Commands

```bash
# Run the application
python main.py

# No build step required - simple Python script
# No test suite set up yet
```

## Dependencies

Standard library only:
- `json` - File persistence (expenses.json)
- `os` - File existence checks
- `datetime` - Timestamps (use `.isoformat()` / `.fromisoformat()` for JSON)
- `csv` - For exporting reports

## JSON Persistence Pattern

```python
def save_to_file(self):
    data = []
    for expense in self.expenses:
        data.append({
            "name": expense.name,
            "amount": expense.amount,
            "category": expense.category,
            "timestamp": expense.timestamp.isoformat()
        })
    with open("expenses.json", "w") as f:
        json.dump(data, f)

def load_from_file(self):
    if not os.path.exists("expenses.json"):
        return
    with open("expenses.json", "r") as f:
        data = json.load(f)
    for item in data:
        expense = Expense(item["name"], item["amount"], item["category"])
        expense.timestamp = datetime.datetime.fromisoformat(item["timestamp"])
        self.expenses.append(expense)
```

## CSV Export Pattern

```python
def export_to_csv(self, filename="report.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Amount", "Category", "Date"])
        for expense in self.expenses:
            writer.writerow([
                expense.name,
                expense.amount,
                expense.category,
                expense.timestamp.strftime("%Y-%m-%d")
            ])
```

## Common Beginner Mistakes to Watch For

- Using `self.append()` instead of `self.expenses.append()`
- Forgetting `self` parameter in method definitions
- Not converting datetime to string before JSON serialization
- Forgetting to subtract 1 from user input for 0-based list indices
- Not handling invalid user input (try/except for int conversion)

## Output Style Requirements

When working with this user:

1. Use TODO(human) comments to mark implementation sections
2. Frame contributions as "Learn by Doing" sections with context, task, and guidance
3. Explain concepts before offering code
4. Wait for user to write code before reviewing

---

## Project Completion Summary

### Project Details
**Project:** Expense Tracker - Command-line expense logging and reporting application
**Status:** ✅ Complete
**Date:** March 2026

### What Was Implemented

1. **Expense Class**
   - `__init__()` with name, amount, category, and auto-generated date
   - `display()` method with formatted table output using f-strings

2. **ExpenseManager Class**
   - `add_expense()` - Create and store Expense objects
   - `view_expenses_category()` - Sub-menu with alphabetical sorting, filter by category
   - `view_expenses_month()` - Sub-menu with reverse chronological sorting, filter by month/year
   - `save_to_file()` - CSV export with headers
   - `load_from_file()` - CSV import with proper type conversion

3. **UI Improvements**
   - Box-drawn menu interface with borders
   - Table-formatted expense display with headers and totals
   - Unicode box characters for visual appeal
   - Consistent indentation and spacing

### What Was Learnt

- **Classes and Objects:** Creating data classes with `__init__` and methods
- **CSV Handling:** `csv.writer()` and `csv.reader()` with `newline=""`
- **Datetime:** `strftime()` for formatting, `strptime()` for parsing, `.today()` for current date
- **Sorting:** Using `sorted()` with tuples, `reverse=True` for descending order
- **String Formatting:** f-strings with alignment (`:<20` for left, `:>8` for right), `:.2f` for decimals
- **File I/O:** `os.path.isfile()` checks, context managers (`with` statements)
- **Type Conversion:** Converting strings to float when loading from CSV
- **List Comprehensions:** Extracting elements from tuples `[m[2] for m in month_data]`

### What Claude (Kimi K2.5 via Ollama) Helped With

- Architecture guidance (three-part design pattern)
- CSV implementation patterns and best practices
- Debugging type conversion issues (float vs string amounts)
- Date formatting and parsing techniques
- Sorting strategies for chronological ordering
- UI table formatting with box-drawing characters
- Explaining f-string formatting syntax
- Fixing `with` block scope issues in `load_from_file()`
- Code review and identifying bugs