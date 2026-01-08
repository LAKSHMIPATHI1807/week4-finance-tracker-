from finance_tracker.expense import Expense
from finance_tracker.reports import (
    expense_statistics,
    month_wise_statistics,
    category_breakdown
)

def sample_expenses():
    return [
        Expense("2026-01-01", 500, "Food", "Breakfast"),
        Expense("2026-01-02", 1000, "Transport", "Train"),
        Expense("2026-01-15", 1500, "Food", "Dinner"),
    ]

def test_expense_statistics():
    expenses = sample_expenses()
    stats = expense_statistics(expenses)

    assert stats["total"] == 3000
    assert stats["count"] == 3
    assert stats["maximum"] == 1500
    assert stats["minimum"] == 500

def test_month_wise_statistics():
    expenses = sample_expenses()
    monthly = month_wise_statistics(expenses)

    assert "2026-01" in monthly
    assert monthly["2026-01"] == 3000

def test_category_breakdown():
    expenses = sample_expenses()
    categories = category_breakdown(expenses)

    assert categories["Food"] == 2000
    assert categories["Transport"] == 1000
