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
        yearly_expense_calendar = {}
        yearly_income_calendar = {}
        self.year = year
        for month in range(1, 13):
            for day in cal.itermonthdates(year, month):
                if day.year == year:
                    yearly_expense_calendar[day] = []
                    yearly_income_calendar[day] = []

        self.expense_calendar = yearly_expense_calendar
        self.income_calendar = yearly_income_calendar
    
    def add_expenditure(self, date, spending):
        """Adds an Expenditure object to the corresponding date

        Args:
            date (Date object): Date the expense was made
            spending (Expenditure object): The expenditure that was made
        
        Side Effect:
            Adds the Expenditure object into the list which is the value for corresponding Date key in the self.expense_calendar dictionary
        """
        
        self.expense_calendar[date].append(spending)


    def add_fixed_expenditure(self, date, spending, pays_every):
        """Adds a reoccurring Expenditure object to corresponding dates

        Args:
            date (Date object): Date the expense was first made
            spending (Expenditure object): The expenditure that was made
            pays_every (String): String that tells how often the expenditure occurs
        
        Side Effect:
            Adds the Expenditure object into the list which is the value for corresponding Date keys in the self.expense_calendar dictionary
        """
        if pays_every.casefold() == "yearly".casefold(): # Yearly Payment
            self.add_expenditure(date, spending)
        else: # Monthly Payment
            for new_month in range(date.month, 13): # Adds payment to same day of every month starting from the passed in date
                new_date = date.replace(month = new_month)
                self.add_expenditure(new_date, spending)

    
    def get_daily_spending_amount(self, date):
        """Calculates total amount of money spent on particular date

        Args:
            date (Date object): Date to get the total amount of money spent for
        
        Returns:
            total_spent (Decimal object): The total amount of money spent on the passed in date
        """
        total_spent = 0

        for spending in self.expense_calendar[date]:
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
    
    def add_income(self, date, income):
        """Adds an Income object to the corresponding date

        Args:
            date (Date object): Date the income was paid
            income (Income object): The income that was paid
        
        Side Effect:
            Adds the Income object into the list which is the value for corresponding Date key in the self.income_calendar dictionary
        """
        self.income_calendar[date].append(income)
    
    def add_fixed_income(self, date, income, paid_every):
        """Adds an reoccurring Income object to corresponding dates

        Args:
            date (Date object): Date the income was first paid
            income (Income object): The income that was paid
            paid_every (String): String that tells how often the income occurs
        
        Side Effect:
            Adds the Income object into the list which is the value for corresponding Date keys in the self.income_calendar dictionary
        """
        if paid_every.casefold() == "yearly".casefold(): # Yearly Income
            self.add_income(date, income)
        else: # Monthly Income
            for new_month in range(date.month, 13): # Adds income to same day of every month starting from the passed in date
                new_date = date.replace(month = new_month)
                self.add_income(new_date, income)
    
    def get_daily_income_amount(self, date):
        """Calculates total amount of money gained on particular date

        Args:
            date (Date object): Date to get the total amount of money gained for
        
        Returns:
            total_income (Decimal object): The total amount of money gained on the passed in date
        """
        total_income = 0

        for income in self.income_calendar[date]:
            total_income += income.amount
        
        return total_income
    
    def get_total_income_amount_between_two_dates(self, starting_date, end_date):
        """Calculates total amount of money gained between two particular dates

        Args:
            starting_date (Date object): Starting date of the range in which to get the total income for
            end_date (Date object): Ending date of the range in which to get the total income for

        Returns:
            total_gained (Decimal object): The total amount of money gained during the two particular dates that were passed in
        """
        current_date = starting_date
        total_gained = 0
        while current_date <= end_date:
            total_gained += self.get_daily_income_amount(current_date)
            current_date += dt.timedelta(days=1)
        
        return total_gained 
    
    def get_daily_change_in_fund(self, date):
        """Calculates total change in fund on particular date

        Args:
            date (Date object): Date that the changes will be calculated for

        Returns:
            total_change (Decimal Object): Total change occurred on amount of fund on that date
        """
        total_change = self.get_daily_income_amount(date) - self.get_daily_spending_amount(date)

        return total_change

    def get_total_fund_left_between_two_dates(self, starting_date, end_date):
        """Calculates total amount of change in fund between two particular dates

        Args:
            starting_date (Date object): Starting date of the range in which to get the total change for
            end_date (Date object): Ending date of the range in which to get the total change for

        Returns:
            total (Decimal object): The total amount of change in funds during the two particular dates that were passed in
        """
        total = self.get_total_income_amount_between_two_dates(starting_date, end_date) - self.get_total_spending_amount_between_two_dates(starting_date, end_date)
        
        return total
    
    def get_recommended_daily_budget(self, starting_date, end_date):
        total_fund = self.get_total_fund_left_between_two_dates(dt.date(self.year,1,1), end_date)
        num_of_days = abs((end_date - starting_date).days) + 1
        
        return truncate_to_hundredths(total_fund / num_of_days)

class Expenditure:
    """Class for all expenditure of the user

    Attributes:
        description (String): Description of the expenditure. i.e. Spotify membership, Car insurance, etc.
        amount (float): Amount of the expenditure in dollars
        type (String): Whether if it is a fixed expenditure or not
        category (String): What category the expenditure is for. i.e. Leisure, food, hobby, etc.
    """
    def __init__(self, description, amount, type, category):
        self.description = description
        self.amount = decimal.Decimal(str(amount))
        self.type = type
        self.category = category
    
    def __repr__(self):
        return f"{self.description}\nAmount: {self.amount}$\nType: {self.type}\nCategory: {self.category}"

class Income:
    """Class for all income of the user

    Attributes:
        description (String): Description of the income. i.e. Pocket money, parttime job, etc
        amount (float): Amount of the income in dollars
        type (String): Whether if it is a fixed income or not
    """
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = decimal.Decimal(str(amount))
        self.type = type
    
    def __repr__(self):
        return f"{self.description}\nAmount: {self.amount}$\nType: {self.type}"

