class Budget:
    def __init__(self, available_funds):
        self.available_funds = available_funds
        self.fixed_expenses = {} #saves fixed cost items, name:cost
        self.spend_categories = {} #saves specific spend categories, category:percentage
    
    def add_category(self, name, percentage):
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
