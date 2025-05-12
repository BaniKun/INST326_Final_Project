import datetime as dt
import pytest
import calendar as cl   
import pickle            
from decimal import Decimal
from classes import Budget_Calendar, Expenditure, Income

# Fixture that provides a Budget_Calendar for 2025.
@pytest.fixture
def budget_calendar():
    return Budget_Calendar(2025)

def test_init(budget_calendar):
    """Test that Budget_Calendar initializes correctly."""
    assert isinstance(budget_calendar, Budget_Calendar)
    assert isinstance(budget_calendar.expense_calendar, dict)
    assert isinstance(budget_calendar.income_calendar, dict)

def test_add_expenditure(budget_calendar):
    """Test adding a new expense."""
    date = dt.date(2025, 8, 3)
    expense = Expenditure("Birthday Cake", Decimal("65.00"), "Food", "Entertainment")
    
    budget_calendar.add_expenditure(date, expense)
    assert expense in budget_calendar.expense_calendar.get(date, [])

def test_add_fixed_expenditure(budget_calendar):
    """Test adding a fixed (recurring) expense."""
    date = dt.date(2025, 1, 1)
    expense = Expenditure("Phone Plan", Decimal("80.00"), "Utilities", "Monthly Bill")
    
    budget_calendar.add_fixed_expenditure(date, expense, "monthly")
    
    for month in range(1, 13):
        day = dt.date(2025, month, 1)
        assert expense in budget_calendar.expense_calendar.get(day, [])

@pytest.mark.parametrize("start_date, end_date, expected", [
    (dt.date(2025, 8, 3), dt.date(2025, 8, 4), Decimal("121.78")),
    (dt.date(2025, 8, 3), dt.date(2025, 8, 5), Decimal("121.78")),
    (dt.date(2025, 8, 3), dt.date(2025, 8, 6), Decimal("121.78")),
])

def test_total_spending_amount_between_dates(budget_calendar, start_date, end_date, expected):
    """Test retrieving total spending between two dates."""
    expense = Expenditure("Dinner", expected, "Food", "Dining Out")
    budget_calendar.add_expenditure(start_date, expense)
    
    total = budget_calendar.get_total_spending_amount_between_two_dates(start_date, end_date)
    assert total == expected

def test_add_income(budget_calendar):
    """Test adding an income entry."""
    date = dt.date(2025, 8, 3)
    income = Income("Salary", Decimal("2150.00"), "Job")
    
    budget_calendar.add_income(date, income)
    assert income in budget_calendar.income_calendar.get(date, [])

def test_get_daily_income_amount(budget_calendar):
    """Test retrieving daily income amount."""
    date = dt.date(2025, 8, 3)
    income = Income("Salary", Decimal("2150.00"), "Job")
    
    budget_calendar.add_income(date, income)
    daily_income = budget_calendar.get_daily_income_amount(date)
    assert daily_income == Decimal("2150.00")

def test_get_daily_change_in_fund(budget_calendar):
    """Test calculating the daily change in funds."""
    date = dt.date(2025, 8, 3)
    income = Income("Salary", Decimal("2150.00"), "Job")
    expense = Expenditure("Phone Plan", Decimal("80.00"), "Utilities", "Monthly Bill")
    
    budget_calendar.add_income(date, income)
    budget_calendar.add_expenditure(date, expense)
    daily_change = budget_calendar.get_daily_change_in_fund(date)
    
    assert daily_change == Decimal("2070.00")
