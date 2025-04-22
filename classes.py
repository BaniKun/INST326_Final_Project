import calendar as cl
import datetime as dt
import math
import decimal

def truncate_to_hundredths(number):
  return math.floor(number * 100) / 100

class Budget_Calendar:
    """Class for a Budget Calendar Object. A budget calendar is a dictionary with date objects as keys and list of Expenditure object as values.

    Attributes:
        calendar (dictionary): Dictionary with date objects as keys and list of Expenditure object as values
    """
    def __init__(self, year):
        """Initializes a Budget_Calendar object.

        Args:
            year (int): The year the calendar will be on
        """
        cal = cl.Calendar()
        yearly_calendar = {}
        for month in range(1, 13):
            for day in cal.itermonthdates(year, month):
                if day.year == year:
                    yearly_calendar[day] = []

        self.calendar = yearly_calendar
    
    def add_expenditure(self, date, spending):
        """Adds an Expenditure object to the corresponding date

        Args:
            date (Date object): Date the expense was made
            spending (Expenditure object): The expenditure that was made
        
        Side Effect:
            Adds the Expenditure object into the list which is the value for corresponding Date key in the self.calendar dictionary
        """
        self.calendar[date].append(spending)
    
    def get_daily_spending_amount(self, date):
        """Calculates total amount of money spent on particular date

        Args:
            date (Date object): Date to get the total amount of money spent for
        
        Returns:
            total_spent (Decimal object): The total amount of money spent on the passed in date
        """
        total_spent = 0

        for spending in self.calendar[date]:
            total_spent += spending.amount
        
        return total_spent
    
    def get_total_spending_amount_between_two_dates(self, starting_date, end_date):
        """Calculates total amount of money spend between two particular dates

        Args:
            starting_date (Date object): Starting date of the range in which to get the total spending for
            end_date (Date object): Ending date of the range in which to get the total spending for

        Returns:
            total_spent (Decimal object): The total amount of money spent during the two particular dates that were passed in
        """
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
    def __init__(self, description, amount, type, category):
        self.description = description
        self.amount = decimal.Decimal(str(amount))
        self.type = type
        self.category = category
    
    def __repr__(self):
        return f"Date: {self.date}\n{self.description}\nAmount: {self.amount}$\nType: {self.type}\nCategory: {self.category}"

def calculate_daily_budget(fund, start_date, end_date):
    days_between = (end_date - start_date).days + 1
    
    return fund / days_between

if __name__ == "__main__":
    """
    myBudget_recommendation = Budget_recommendation(1200, "monthly", 2, 2025)
    print(myBudget_recommendation)

    myExpenditure1 = Expenditure("Spotify", 9.99, "Fixed", "Music", dt.date(2025, 4, 22))
    myExpenditure2 = Expenditure("Spotify", 9.99, "Fixed", "Music", dt.date(2025, 4, 23))
    print(myExpenditure1)
    print([myExpenditure1, myExpenditure2])


    myBudget = calculate_daily_budget(1200, dt.date(2025, 4, 1), dt.date(2025, 4, 30))
    print(myBudget)
    """

    myBudget_Calendar = Budget_Calendar(2025)
    myBudget_Calendar.add_expenditure(dt.date(2025,4,22), Expenditure("Spotify", 9.99, "Fixed", "Music"))
    myBudget_Calendar.add_expenditure(dt.date(2025,4,22), Expenditure("Spotify", 20.99, "Fixed", "Music"))
    myBudget_Calendar.add_expenditure(dt.date(2025,4,23), Expenditure("Spotify", 30.99, "Fixed", "Music"))
    print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,4,22)))
    print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,4,23)))
    print(myBudget_Calendar.get_total_spending_amount_between_two_dates(dt.date(2025,4,22), dt.date(2025,4,23)))