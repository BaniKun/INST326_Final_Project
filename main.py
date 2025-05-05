# File for main function to run the app
import classes

class User_Interface:
    def __init__(self):
        self.welcome()
        self.main_menu()

    def welcome(self):
        print("------------------------------------------------------------")
        print("Welcome to your Budget Calendar!")
        print("------------------------------------------------------------")
    
    def main_menu(self):
        print("What would you like to do?\n - Add Income\n - Add Expense\n - Calculate")
        print("------------------------------------------------------------")

        user_input = input()
        wrong_input = True

        while wrong_input:
            if user_input.casefold() == "Add Income".casefold():
                self.add_income_prompt()
                wrong_input = False
            elif user_input.casefold() == "Add Expense".casefold():
                self.add_expense_prompt()
                wrong_input = False
            elif user_input.casefold() == "Calculate".casefold():
                self.calculate_prompt()
                wrong_input = False
            else:
                print("Please enter correctly")

    
    def add_income_prompt(self):
        print("This is the income prompt")

    def add_expense_prompt(self):
        print("This is the expense prompt")

    def calculate_prompt(self):
        print("This is the calculate prompt")





if __name__ == "__main__":
    launch = User_Interface()