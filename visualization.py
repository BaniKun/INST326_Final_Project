import matplotlib.pyplot as plt
#import seaborn as sns
import datetime as dt

from classes import Budget_Calendar, Expenditure, Income

#sns.set(style="whitegrid", font="sans-serif")

class BudgetVisualizer:
    """A class to create a few different visualizations from a Budget_Calendar object.
    Attributes: 
        - budget (Budget_Calendar): The budget calendar containing the expense and income data.
    """
    def __init__(self, budget):
        self.budget = budget

    def plot_daily_spending(self, start_date, end_date):
        """Creates a line plot of daily spending between the start and end dates.
        Args:
            - start_date (date): The start date.
            - end_date (date): The end date.
        """
        current_date = start_date
        dates, spending = [], []

        while current_date <= end_date:
            dates.append(current_date)
            amount = self.budget.get_daily_spending_amount(current_date)
            spending.append(float(amount))  
            current_date += dt.timedelta(days=1)

        plt.figure(figsize=(8, 4))
        plt.plot(dates, spending, marker='o', linestyle='-', color='orchid')
        plt.title(f"Daily Spending\n{start_date} to {end_date}")
        plt.xlabel("Date")
        plt.ylabel("Spending ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_daily_income(self, start_date, end_date):
        """
        Creates a line plot of daily income between start_date and end_date.
        
        Args:
            - start_date (date): The starting date
            - end_date (date): The ending date
        """
        current_date = start_date
        dates, income_values = [], []
        
        while current_date <= end_date:
            dates.append(current_date)
            amount = self.budget.get_daily_income_amount(current_date)
            income_values.append(float(amount))
            current_date += dt.timedelta(days=1)
        
        plt.figure(figsize=(8, 4))
        plt.plot(dates, income_values, marker='o', linestyle='-', color='skyblue')
        plt.title(f"Daily Income\n{start_date} to {end_date}")
        plt.xlabel("Date")
        plt.ylabel("Income ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_expenditure_category_distribution(self):
        """Creates a pie chart showing the percentage distribution of expenditures by category"""
        category_totals = {}

        for date, expenditures in self.budget.expense_calendar.items():
            for exp in expenditures:
                category = exp.category
                category_totals[category] =category_totals.get(category, 0) + float(exp.amount)
        
        if not category_totals:
            print("No expenditure data available to plot.")
            return
        
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        color = 'pink', 'slateblue', 'mediumpurple', 'palevioletred', 'thistle', 'plum', 'honeydew', 'lightcoral', 'darkcyan'

        plt.figure(figsize=(6, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=color)
        plt.title("Expenditure Distribution by Category")
        plt.axis("equal") 
        plt.show()


if __name__ == "__main__":
    budget_calendar = Budget_Calendar(2025)
    
    sample_date1 = dt.date(2025, 5, 12)
    sample_date2 = dt.date(2025, 5, 20)
    sample_date3 = dt.date(2025, 5, 1)
    sample_date4 = dt.date(2025, 5, 31)
    
    exp1 = Expenditure("Groceries", 150.75, "variable", "Food")
    exp2 = Expenditure("Gym Membership", 50.00, "fixed", "Health")
    exp3 = Expenditure("Snack Run", 15.45, "variable", "Food")
    exp4 = Expenditure("Rent", 1290.00, "fixed", "Housing")

    inc1 = Income("Salary", 2000.00, "fixed")
    inc2 = Income("Freelance", 200.00, "variable")
    inc3 = Income("Clothes Sale", 45.00, "variable")
    inc4 = Income("Financial Aid Refund", 2200.00, "variable")
    
    # Populate the calendar with sample data.
    budget_calendar.add_expenditure(sample_date3, exp4)
    budget_calendar.add_expenditure(sample_date1, exp2)
    budget_calendar.add_expenditure(sample_date2, exp3)
    budget_calendar.add_expenditure(sample_date4, exp1)

    budget_calendar.add_income(sample_date1, inc1)
    budget_calendar.add_income(sample_date2, inc2)
    budget_calendar.add_income(sample_date3, inc3)
    budget_calendar.add_income(sample_date4, inc4)
    
    # Initialize the visualizer with the budget calendar.
    visualizer = BudgetVisualizer(budget_calendar)
    
    # Visualization 1: Plot daily spending for two days.
    visualizer.plot_daily_spending(sample_date3, sample_date4)
    
    # Visualization 2: Plot daily income for two days.
    visualizer.plot_daily_income(sample_date3, sample_date4)
    
    # Visualization 3: Show a pie chart of expenditure categories.
    visualizer.plot_expenditure_category_distribution()