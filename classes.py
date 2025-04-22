import calendar
import datetime

class Budget:
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

        self.set_recommended_budget()
    
    def __repr__(self):
        return f"{self.occurrence} income: {self.income}\nDaily Budget: {self.daily_budget}\nMonthly Budget: {self.monthly_budget}\nYearly Budget: {self.yearly_budget}"

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

            if self.month == 1 | 3 | 5 | 7 | 8 | 10 | 12:
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
    def __init__(self, description, amount, type, category, day, month, year):
        self.description = description
        self.amount = amount
        self.type = type
        self.category = category
        self.date = f"{month}/{day}/{year}"
    
    def __repr__(self):
        return f"Date: {self.date}\n{self.description}\nAmount: {self.amount} $\nType: {self.type}\nCategory: {self.category}"
    
    