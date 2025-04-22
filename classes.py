import calendar as cl
import datetime as dt
import math

def truncate_to_hundredths(number):
  return math.floor(number * 100) / 100

class Budget_Calendar:
    def __init__(self, year):
        cal = cl.Calendar()
        yearly_calendar = {}
        for month in range(1, 13):
            for day in cal.itermonthdates(year, month):
                if day.year == year:
                    yearly_calendar[day] = []

        self.calendar = yearly_calendar
    
    def add_expenditure(self, date, spending):
        self.yearly_calendar[date].append(spending)
    
    def get_daily_spending_amount(self, date):
        total_spent = 0

        for spending in self.yearly_calendar[date]:
            total_spent += spending.amount
        
        return total_spent
    
    def get_total_spending_amount_between_two_dates(self, starting_date, end_date):
        current_date = starting_date
        total_spent = 0
        while current_date <= end_date:
            total_spent += self.get_daily_spending_amount(current_date)
            current_date += dt.timedelta(days=1)
        
        return total_spent


class Budget_recommendation:
    def __init__(self, income, occurrence, month, year):
        
        self.occurrence = occurrence
        self.income = income
        self.daily_budget = 0
        self.monthly_budget = 0
        self.yearly_budget = 0
        self.year = year
        self.month = month
        if year % 4 == 0:
            self.leap_year = True
        else:
            self.leap_year = False

        self.set_recommended_budget()
    
    def __repr__(self):
        return f"{self.occurrence.capitalize()} income: {self.income}\nDaily Budget: {truncate_to_hundredths(self.daily_budget)}\nMonthly Budget: {self.monthly_budget}\nYearly Budget: {self.yearly_budget}"

    def set_recommended_budget(self):
        if self.occurrence.casefold() == "Yearly".casefold():
            self.yearly_budget = self.income

            self.monthly_budget = self.income / 12

            if self.leap_year:
                self.daily_budget = self.income / 366
            else:
                self.daily_budget = self.income / 365

        elif self.occurrence.casefold() == "Monthly".casefold():
            self.yearly_budget = self.income * 12

            self.monthly_budget = self.income

            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                self.daily_budget = self.income / 31
            elif self.month != 2:
                self.daily_budget = self.income / 30
            elif self.leap_year:
                self.daily_budget = self.income / 29
            else:
                self.daily_budget = self.income / 28

        else:
            if self.leap_year:
                self.yearly_budget = self.income * 366
            else:
                self.yearly_budget = self.income * 365
            
            if self.month == 1 | 3 | 5 | 7 | 8 | 10 | 12:
                self.monthly_budget = self.income * 31
            elif self.month != 2:
                self.monthly_budget = self.income * 30
            elif self.leap_year:
                self.monthly_budget = self.income * 29
            else:
                self.monthly_budget = self.income * 28
            
            self.daily_budget = self.income  
    
class Expenditure:
    """Class for all expenditure of the user

    Attributes:
        description (String): Description of the expenditure. i.e. Spotify membership, Car insurance, etc.
        amount (float): Amount of the expenditure in dollars
        type (String): Whether if it is a fixed expenditure or not
        category (String): What category the expenditure is for. i.e. Leisure, food, hobby, etc.
        date (String): Day it was made in the format of month/day/year
    """
    def __init__(self, description, amount, type, category, date):
        self.description = description
        self.amount = amount
        self.type = type
        self.category = category
        self.date = date
    
    def __repr__(self):
        return f"Date: {self.date}\n{self.description}\nAmount: {self.amount}$\nType: {self.type}\nCategory: {self.category}"

def calculate_daily_budget(fund, start_date, end_date):
    days_between = (end_date - start_date).days + 1
    
    return fund / days_between

    
myBudget_recommendation = Budget_recommendation(1200, "monthly", 2, 2025)
print(myBudget_recommendation)

myExpenditure1 = Expenditure("Spotify", 9.99, "Fixed", "Music", dt.date(2025, 4, 22))
myExpenditure2 = Expenditure("Spotify", 9.99, "Fixed", "Music", dt.date(2025, 4, 23))
print(myExpenditure1)
print([myExpenditure1, myExpenditure2])


myBudget = calculate_daily_budget(1200, dt.date(2025, 4, 1), dt.date(2025, 4, 30))
print(myBudget)