# File for main function to run the app
import classes

class User_Interface:
    def __init__(self):
        self.print_line()
        print("Welcome to your Budget Calendar!")
        self.print_line()

        wrong_input = True
        while wrong_input:
            self.print_line()
            print("What year would you like to make a calendar for?")
            self.print_line()
            try: 
                self.year = int(input())
                wrong_input = False
            except:
                print("Please input the year in numbers.")
        
        self.calendar = classes.Budget_Calendar(self.year)
        self.main_menu()

    def print_line(self):
        print("------------------------------------------------------------")        
    
    def main_menu(self):
        wrong_input = True

        while wrong_input:
            self.print_line()
            print("What would you like to do?\n - Add Income\n - Add Expense\n - Calculate")
            self.print_line()
            user_input = input()
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
                print("Please enter correctly.")

    
    def add_income_prompt(self):
        self.print_line()
        print("This is the income prompt")

    def add_expense_prompt(self):
        self.print_line()
        print("This is the expense prompt")

    def calculate_prompt(self):
        self.print_line()
        print("This is the calculate prompt")





if __name__ == "__main__":
    launch = User_Interface()