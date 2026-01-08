import os
import json
from finance_tracker.expense import Expense
from finance_tracker.file_handler import (
    save_expenses,
    load_expenses,
    backup_expenses,
    restore_expenses
)

TEST_DATA_FILE = "data/expenses.json"

def test_save_and_load_expenses():
    expense = Expense("2026-01-10", 300, "Transport", "Bus")
    save_expenses([expense])

    expenses = load_expenses()
    assert len(expenses) > 0
    assert expenses[-1].amount == 300

def test_backup_creation():
    backup_expenses()
    assert os.path.exists("data/backup")

def test_restore_expenses():
    # Create dummy data
    expense = Expense("2026-01-12", 1000, "Shopping", "Clothes")
    save_expenses([expense])

    # Backup
    backup_expenses()

    # Modify data
    save_expenses([])

    # Find latest backup
    backups = os.listdir("data/backup")
    latest_backup = os.path.join("data/backup", backups[-1])

    # Restore
    restore_expenses(latest_backup)
    expenses = load_expenses()

    assert len(expenses) > 0
