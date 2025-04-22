import matplotlib.pyplot as plt
import classes

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
    budget = classes.Budget(2000)
    budget.add_category("Rent", 40)
    budget.add_category("Food", 20)
    budget.set_fixed_expense("Insurance", 300)
    budget.set_fixed_expense("Subscriptions", 100)
    
    budget_summary = budget.calculate_split()
    print(budget_summary)
    
    budget.visualize()
