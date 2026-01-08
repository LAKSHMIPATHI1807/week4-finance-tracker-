Finance Tracker – Week 4 Project

 Project Description
The **Finance Tracker** is a Python-based console application designed to help users track, manage, and analyze their personal expenses.  
It follows a **modular project structure**, uses **Object-Oriented Programming (OOP)** principles, and stores data persistently using **JSON files**.

This project supports:
- Expense management
- Reports and statistics
- Budget tracking
- Backup and restore
- CSV export
- Unit testing

Project Structure

week4-finance-tracker/
│
├── finance_tracker/
│ ├── init.py
│ ├── main.py
│ ├── expense.py
│ ├── expense_manager.py
│ ├── file_handler.py
│ ├── reports.py
│ └── utils.py
│
├── data/
│ ├── expenses.json
│ ├── backup/
│ └── exports/
│
├── tests/
│ ├── test_expense.py
│ ├── test_file_handler.py
│ └── test_reports.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── run.py

---

Detailed File & Folder Explanation

### `finance_tracker/`
Main application package containing all core modules.

#### `__init__.py`
- Marks the folder as a Python package.

#### `main.py`
- Contains the **menu-driven user interface**
- Integrates all modules
- Handles user input and program flow

#### `expense.py`
- Defines the `Expense` class
- Attributes:
  - date
  - amount
  - category
  - description
- Validates input data (date format, positive amount)

#### `expense_manager.py`
- Manages a collection of expenses
- Functions include:
  - Add expense
  - Remove expense
  - View all expenses
  - Search and filter expenses

#### `file_handler.py`
- Handles all file operations:
  - Save and load expenses (JSON)
  - Backup expense data
  - Restore from backup
  - Export expenses to CSV
- Handles file-related errors safely

#### `reports.py`
- Generates analytical reports:
  - Monthly expense summary
  - Category-wise expense breakdown
  - Expense statistics (total, average, min, max)
  - Trend analysis

#### `utils.py`
- Utility/helper functions
- Input validation
- Formatting output
- Common reusable logic

---

### `data/`
Stores all application data.

#### `expenses.json`
- Stores all expense records persistently in JSON format.

#### `backup/`
- Stores timestamped backup files for data recovery.

#### `exports/`
- Stores exported CSV files.

---

### `tests/`
Contains unit tests written using **pytest**.

#### `test_expense.py`
- Tests validation logic of the `Expense` class.

#### `test_file_handler.py`
- Tests file operations such as save, load, backup, and restore.

#### `test_reports.py`
- Tests report calculations and statistics.

---

### `run.py`
- Entry point of the application
- Starts the Finance Tracker program

---

### `requirements.txt`
- Lists required Python dependencies.
