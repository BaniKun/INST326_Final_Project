import pytest
import datetime as dt
import calendar as cl   
import pickle            
from decimal import Decimal
from unittest.mock import patch, MagicMock

from classes import Budget_Calendar, Expenditure, Income
from classes import Expenditure
from classes import Income
from main import User_Interface

# Fixture that creates a Budget_Calendar for 2025.
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


#Test block for Expenditure class
def test_expenditure_creation():
    """Tests creating a new expense and if all aspects of the expense are initiated correctly"""
    exp = Expenditure("Gym Membership", Decimal(45.00), "fixed", "Hobby")

    assert exp.description == "Gym Membership"
    assert exp.amount == Decimal("45.00")
    assert exp.type == "fixed"
    assert exp.category == "Hobby"

def test_expenditure_decimal_conversion():
    exp = Expenditure("Health Insurance", "125.50", "fixed", "Health")

    assert isinstance(exp.amount, Decimal)
    assert exp.amount == Decimal("125.50")

def test_expenditure_repr():
    """Tests the repr"""
    exp = Expenditure("Spotify Membership", 11.99, "fixed", "Leisure")
    expected_repr = "Spotify Membership\nAmount: 11.99$\nType: fixed\nCategory: Leisure"
    
    assert repr(exp) == expected_repr


#Test block for Income class
def test_income_creation():
    """Tests creating a new income entry and if all attributes are correct"""
    income = Income("Babysitting", 150.00, "variable")
    
    assert income.description == "Babysitting"
    assert income.amount == Decimal(150.00)
    assert income.type == "variable"

def test_income_decima_conv():
    """Tests if amount is correctly converted to decimal"""
    income = Income("Birthday Money", "150.00", "variable")

    assert isinstance(income.amount, Decimal)
    assert income.amount == Decimal("150.00")

def test_income_repr(): 
    """Tests if the repr is formatting correctly""" 
    income = Income("Tutoring Job", 50.00, "fixed") 
    expected_repr = f"Tutoring Job\nAmount: {income.amount}$\nType: fixed" 

    assert repr(income) == expected_repr


#Test block for main document
