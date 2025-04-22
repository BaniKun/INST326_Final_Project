import matplotlib.pyplot as plt

class Budget:
    """The Budget class manages a budget with fixed expenses and spending categories."""
    def __init__(self, available_funds):
        """Initializes the budget with available funds and empty expense categories
        Args: 
        - available_funds: the total funds available for the budgeting plan."""
        
        self.available_funds = available_funds
        self.fixed_expenses = {} #saves fixed cost items, name:cost
        self.spend_categories = {} #saves specific spend categories, category:percentage
    
    def add_category(self, name, percentage):
        """Adds a spending category with an allocated percentage
        Args: 
        - name: name of the category
        - percentage: percentage of the remaining budget allocated to that category
        Raises:
        - ValueError: if the percentage is not between 0 and 100."""
        
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.spend_categories[name] = percentage

    def set_fixed_expense(self, name, amount):
        if amount < 0:
            raise ValueError("Expense must be positive.")
        self.fixed_expenses[name] = amount

    def calculate_split(self):
        allocated_funds = sum(self.fixed_expenses.values())
        remaining_budget = self.available_funds - allocated_funds

        if remaining_budget < 0:
            raise ValueError("Expenses exceed total available funds!")
        budget_splits = {
            name: (percentage / 100) * remaining_budget
            for name, percentage in self.spend_categories.items()
        }

        return {
            "Fixed Expenses":self.fixed_expenses,
            "Spend Category Allocations" :budget_splits,
            "Remaining Budget" :remaining_budget
        }

    def visualize(self):
        budget_data = self.calculate_split()
        remaining_budget = budget_data["Remaining Budget"]
    
        categories = list(self.spend_categories.keys())  + list(self.fixed_expenses.keys()) + ["Remaining Budget"]
        percentages = list(self.spend_categories.values()) + list(self.fixed_expenses.values()) + [remaining_budget]

        plt.figure(figsize=(8,8))
        colors = ['#9A133DFF', '#B93961FF', '#D8527CFF', '#F28AAAFF', '#F9B4C9FF', '#F9E0E8FF', '#FFFFFFFF', '#EAF3FFFF', '#C5DAF6FF', '#A1C2EDFF', '#6996E3FF', '#4060C8FF', '#1A318BFF']
        #color palette from: https://python-graph-gallery.com/color-palette-finder/
        plt.pie(percentages, labels=categories, colors=colors)
        plt.title("Budget Allocation")
        plt.show()

if __name__ == "__main__":
    budget = Budget(2000)
    budget.add_category("Rent", 40)
    budget.add_category("Food", 20)
    budget.set_fixed_expense("Insurance", 300)
    budget.set_fixed_expense("Subscriptions", 100)
    
    budget_summary = budget.calculate_split()
    print(budget_summary)
    
    budget.visualize()
