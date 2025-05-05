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
        """A method that prints out a dash line

        Side Effect:
            Prints out a line with 60 dashes
        """
        print("------------------------------------------------------------")        
    
    def main_menu(self):
        """A method that prompts the main menu to the user

        Side Effect:
            Prompts the user between adding income or expense, or run a calculation on the Calendar.
        """
        wrong_input = True

        while wrong_input:
            self.print_line()
            print("What would you like to do?\n - Add Income\n - Add Expense\n - Calculate Funds")
            self.print_line()
            user_input = input()
            if user_input.casefold() == "Add Income".casefold(): # If the user chooses to add income to the calendar
                self.add_income_prompt()
                wrong_input = False
            elif user_input.casefold() == "Add Expense".casefold(): # If the user chooses to add expense to the calendar
                self.add_expense_prompt()
                wrong_input = False
            elif user_input.casefold() == "Calculate Funds".casefold(): # If the user chooses to calculate funds on the calendar
                self.calculate_prompt()
                wrong_input = False
            else: # If the user input does not match any of the options
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