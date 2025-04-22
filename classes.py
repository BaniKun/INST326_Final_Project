import calendar
import datetime as dt
import math

def truncate_to_hundredths(number):
  return math.floor(number * 100) / 100

class Budget_recommendation:
    """The Budget class manages a budget with fixed expenses and spending categories."""
    def __init__(self, income, occurrence, month, year):
        """Initializes the budget with available funds and empty expense categories
        Args: 
            income (float): Incoming amount of funds in dollars
            occurrance (String): How often the user receives income. i.e. daily / weekly / yearly
        """
        
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
    
    
            
class Budget:
    def __init__(self, fund, date1, date2):
        self.total_fund = fund
        self.start_date = date1
        self.end_date = date2
    
    def calculate_daily_budget(self):
        days_between = (self.end_date - self.start_date).days + 1
        
        return self.total_fund / days_between
        
        
    
    
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
    
myBudget_recommendation = Budget_recommendation(1200, "monthly", 2, 2025)
print(myBudget_recommendation)

myExpenditure = Expenditure("Spotify", 9.99, "Fixed", "Music", dt.date(2025, 4, 22))
print(myExpenditure)

myBudget = Budget(1200, dt.date(2025, 4, 1), dt.date(2025, 4, 30))
print(myBudget.calculate_daily_budget())