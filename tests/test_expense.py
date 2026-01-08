import pytest
from finance_tracker.expense import Expense

def test_valid_expense_creation():
    expense = Expense("2026-01-10", 500, "Food", "Lunch")
    assert expense.amount == 500
    assert expense.category == "Food"
    assert expense.description == "Lunch"

def test_invalid_date_format():
    with pytest.raises(ValueError):
        Expense("10-01-2026", 200, "Food", "Invalid date")

def test_negative_amount():
    with pytest.raises(ValueError):
        Expense("2026-01-10", -100, "Food", "Negative amount")

def test_zero_amount():
    with pytest.raises(ValueError):
        Expense("2026-01-10", 0, "Food", "Zero amount")