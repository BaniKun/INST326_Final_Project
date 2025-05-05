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
        """Adds an reoccurring Expenditure object to corresponding dates

        Args:
            date (Date object): Date the expense was first made
            spending (Expenditure object): The expenditure that was made
            pays_every (String): String that tells how often the expenditure occurs
        
        Side Effect:
            Adds the Expenditure object into the list which is the value for corresponding Date keys in the self.expense_calendar dictionary
        """
        if pays_every == "yearly": # Yearly Payment
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
        if paid_every == "yearly": # Yearly Income
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
            total_spent += self.get_daily_income_amount(current_date)
            current_date += dt.timedelta(days=1)
        
        return total_gained 
    
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
        return f"{self.description}\nAmount: {self.amount}$\nType: {self.type}\nCategory: {self.category}"

def calculate_daily_budget(fund, start_date, end_date):
    days_between = (end_date - start_date).days + 1
    
    return fund / days_between

class Income:
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.type = type
    
    def __repr__(self):
        return f"{self.description}\nAmount: {self.amount}$\nType: {self.type}"

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
    print(dt.date(2025,4,23).month)
    for i in range(4, 12):
        print(i)
    myBudget_Calendar.add_fixed_expenditure(dt.date(2025,4,25), Expenditure("Spotify", 9.99, "Fixed", "Music"), "monthly")
    print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,4,25)))
    print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,5,25)))
    print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,12,25)))
    print(myBudget_Calendar.get_total_spending_amount_between_two_dates(dt.date(2025,4,25), dt.date(2025,5,25)))
    