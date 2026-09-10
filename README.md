# Personal Finance Manager

A Python-based personal finance management system for tracking income, expenses, categories, budgets, and financial summaries.

This project was built as a practical Python project to apply object-oriented programming, data structures, input validation, exception handling, and Git/GitHub workflows.

## Features

* Add income with amount, description, and income type
* Add expenses with amount, description, and category
* Add and view spending categories
* Add and view budgets
* View all recorded transactions
* Calculate current balance
* Track spending by category
* Generate a financial summary
* Validate user input and handle invalid entries
* Exit the application safely

## Python Concepts Used

* Variables and data types
* Strings
* Lists
* Dictionaries
* Conditions
* Loops
* Functions and methods
* Exception handling
* Object-Oriented Programming (OOP)
* Classes and objects
* Inheritance
* Abstraction
* `super()`
* `isinstance()`
* List and dictionary manipulation
* `datetime`

## Project Structure

```text
Personal Finance Manager
│
├── Income
├── Expenses
├── Categories
├── Budgets
├── Transactions
└── Financial Reports
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/KelvinWambui/personal-finance-manager.git
```

### 2. Navigate into the project

```bash
cd personal-finance-manager
```

### 3. Run the application

```bash
python personal_finance_manager.py
```

## Example

The application provides an interactive menu:

```text
===== PERSONAL FINANCE MANAGER =====

Please Select a choice

1. Add Income
2. Add Expense
3. Add Category
4. View Transactions
5. View Balance
6. Add Budget
7. View Spending by Category
8. Financial Summary
9. View Categories
10. View Budgets
11. Exit
```

## Current Version

**Version 1.0**

The current version stores data in memory while the application is running. Data is reset when the program is restarted.

Future versions may introduce persistent storage using files, JSON, or a database.

## What I Learned

This project helped me move from practicing individual Python concepts to combining them into a complete working application.

It also gave me practical experience using Git and GitHub to track changes, create commits, and maintain a project repository.

## Future Improvements

* Persistent data storage
* Database integration
* Better transaction reporting
* Monthly financial reports
* Budget tracking against actual spending
* Improved user interface
* Automated testing

## Author

**Kelvin Wambui**

Bachelor's Degree in Information Technology

Building practical Python projects while progressing toward AI Application Engineering.
