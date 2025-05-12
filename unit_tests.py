import datetime as dt
import pytest

from classes import Budget_Calendar
from classes import Expenditure, Income

@pytest.fixture
def TEST_Budget_Calendar():
    """Fixture to create an instance of Budget_Calendar to test.
        - Will create the 2025 calendar"""
    return Budget_Calendar(2025);

def TEST_init(budget_calendar):
    """Tests to ensure Budget_Calendar is initialized correctly."""
    assert isinstance(budget_calendar, Budget_Calendar)
    assert isinstance(budget_calendar.expense_calendar, dict)
    assert isinstance(budget_calendar.income_calendar, dict)

def TEST_add_expenditure(budget_calendar):
    """Test adding a new expense."""
    date = dt.date(2025, 8, 3)
    expense = Expenditure("Birthday Cake", 65.00)

    budget_calendar.add_expenditure(date, expense)
    assert expense in budget_calendar.expense_calendar[date]

def TEST_add_fixed_expenditure(budget_calendar):
    """Test adding a fixed expense."""
    date = dt.date(2025, 1, 1)
    expense = Expenditure("Phone Plan", 80.00)

    budget_calendar.add_fixed_expenditure(date, expense, "monthly")

    for month in range (1, 13):
        assert expense in budget_calendar.expense_calendar[dt.date(2025, month, 1)]

def TEST_get_daily_spending_amount(budget_calendar):
    """Testing to see if the correct daily spending amount is correct and can be retrieved."""
    date = dt.date(2025, 8, 3)
    expense_1 = Expenditure("Birthday Cake", 65.00)
    expense_2 = Expenditure("Snacks at 7-Eleven", 11.78)
    expense_3 = Expenditure("Grocery Run", 45.00)
   
    budget_calendar.add_expenditure(date, expense_1)
    budget_calendar.add_expenditure(date, expense_2)
    budget_calendar.add_expenditure(date, expense_3)

    assert budget_calendar.get_daily_spending_amount(date) == 121.78