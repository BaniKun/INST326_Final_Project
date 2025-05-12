import datetime as dt
import pytest

from classes import Budget_Calendar
from classes import Expenditure, Income

@pytest.fixture
def test_Budget_Calendar():
    """ test calendar """
    return Budget_Calendar(2025);

