# File for main function to run the app
import classes
import pickle
import datetime as dt

class User_Interface:
    def __init__(self):
        self.print_line()
        print("Welcome to your Budget Calendar!")

        wrong_input = True
        while wrong_input:
            self.print_line()
            print("Would you like to load a existing calendar? (Yes/No)")
            user_input = input()
            if user_input.casefold() == "Yes".casefold():
                self.load_calendar()
                wrong_input = False
            elif user_input.casefold() == "No".casefold():
                wrong_second_input = True
                while wrong_second_input:
                    self.print_line()
                    print("What year would you like to make a calendar for?")
                    try: 
                        self.year = int(input())
                        self.calendar = classes.Budget_Calendar(self.year)
                        wrong_second_input = False
                    except:
                        self.print_line()
                        print("Please input the year in numbers.")
                    
                    wrong_input = False
            else:
                self.print_line()
                print("Please enter either yes or no.")
        
        self.main_menu()

    def print_line(self):
        """A method that prints out a dash line

        Side Effect:
            Prints out a line with 60 dashes :')
        """
        print("------------------------------------------------------------")        
    
    def save_calendar(self):
        self.print_line()
        filename = input("Enter the filename you want to save your calendar as: ")
        filename += ".pkl"
        with open(filename, 'wb') as file:
            pickle.dump(self.calendar, file)

    def load_calendar(self):
        wrong_input = True
        while wrong_input:
            self.print_line()
            filename = input("Enter the filename of the calendar that you want to open: ")
            try:
                with open(filename, 'rb') as file:
                    self.calendar = pickle.load(file)
                print("Calendar loaded successfully.")
                wrong_input = False
            except:
                print("Please enter the correct filename.")

        

    def main_menu(self):
        """A method that prompts the main menu to the user

        Side Effect:
            Prompts the user between adding income or expense, or run a calculation on the Calendar.
        """
        wrong_input = True

        while wrong_input:
            self.print_line()
            print("What would you like to do?\n - Add Income\n - Add Expense\n - Calculate Funds\n - Save Calendar\n - Quit")
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
            elif user_input.casefold() == "Save Calendar".casefold(): # If the user chooses to calculate funds on the calendar
                self.save_calendar()
                wrong_input = False
            elif user_input.casefold() == "Quit".casefold(): # If the user chooses to calculate funds on the calendar
                quit()
            else: # If the user input does not match any of the options
                self.print_line()
                print("Please enter correctly.")

    
    def add_expense_prompt(self):
        self.print_line()
        additional_log = True
        while additional_log:
            wrong_input = True
            while wrong_input:
                print("Would you like to add a single expense or a fixed expense? (single/fixed)")
                user_input = input()
                if user_input.casefold() == "single".casefold():
                    description = input("Describe your expense. (i.e. Mcdonalds)\n")
                    wrong_date_input = True
                    while wrong_date_input:
                        try:
                            date_input = input("When was this expense made?(Input in MM/DD/YYYY format)\n")
                            date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                            wrong_date_input = False
                        except:
                            print("Please input the date correctly.")
                    amount = input("How much did you spend?\n")
                    expense_type = "not fixed"
                    category = input("What category does it fall into? (i.e. Food, Hobby, etc)\n")

                    new_expense = classes.Expenditure(description, amount, expense_type, category)

                    self.calendar.add_expenditure(date, new_expense)
                    wrong_input = False
                
                elif user_input.casefold() == "fixed".casefold():
                    description = input("Describe your expense. (i.e. Mcdonalds)\n")
                    wrong_date_input = True
                    while wrong_date_input:
                        try:
                            date_input = input("When was this expense made for the first time? (Input in MM/DD/YYY format)\n")
                            date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                            wrong_date_input = False
                        except:
                            print("Please input the date correctly.")
                    amount = input("How much is each payment?\n")
                    wrong_frequence_input = True
                    while wrong_frequence_input:
                        frequence = input("How often do you make this payment? (monthly/yearly)\n")
                        if frequence.casefold() == "yearly".casefold() or "monthly".casefold():
                            expense_type = frequence
                            wrong_frequence_input = False
                        else:
                            print("Please input the frequence correctly.")
                    category = input("What category does it fall into? (i.e. Food, Hobby, etc)\n")

                    new_expense = classes.Expenditure(description, amount, expense_type, category)

                    self.calendar.add_fixed_expenditure(date, new_expense)
                    wrong_input = False
                
                else:
                    print("Please type in either single or fixed.")
            
            wrong_input = True
            while wrong_input:
                one_more = input("Would you like to add another expense? (Yes/No)\n")
                if one_more.casefold() == "No".casefold():
                    wrong_input = False
                    additional_log = False
                elif one_more.casefold() == "Yes".casefold():
                    wrong_input = False
                else:
                    print("Please type either yes or no.")


    def add_income_prompt(self):
        self.print_line()
        additional_log = True
        while additional_log:
            wrong_input = True
            while wrong_input:
                print("Would you like to add a single income or a fixed income? (single/fixed)")
                user_input = input()
                if user_input.casefold() == "single".casefold():
                    description = input("Describe your income. (i.e. Allowance)\n")
                    wrong_date_input = True
                    while wrong_date_input:
                        try:
                            date_input = input("When was this income paid? (Input in MM/DD/YYY format)\n")
                            date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                            wrong_date_input = False
                        except:
                            print("Please input the date correctly.")
                    amount = input("How much did you gain?\n")
                    income_type = "not fixed"

                    new_income = classes.Income(description, amount, income_type)

                    self.calendar.add_income(date, new_income)
                    wrong_input = False
                
                elif user_input.casefold() == "fixed".casefold():
                    description = input("Describe your income. (i.e. Allowance)\n")
                    wrong_date_input = True
                    while wrong_date_input:
                        try:
                            date_input = input("When was this income paid for the first time?(Input in MM/DD/YYY format)\n")
                            date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                            wrong_date_input = False
                        except:
                            print("Please input the date correctly.")
                    amount = input("How much is each payment?\n")
                    wrong_frequence_input = True
                    while wrong_frequence_input:
                        frequence = input("How often do you get paid this payment? (monthly/yearly)\n")
                        if frequence.casefold() == "yearly".casefold() or "monthly".casefold():
                            income_type = frequence
                            wrong_frequence_input = False
                        else:
                            print("Please input the frequence correctly.")

                    new_income = classes.Income(description, amount, income_type)

                    self.calendar.add_fixed_income(date, new_income)
                    wrong_input = False

                else:
                    print("Please type in either single or fixed.")
        
            wrong_input = True
            while wrong_input:
                one_more = input("Would you like to add another expense? (Yes/No)\n")
                if one_more.casefold() == "No".casefold():
                    wrong_input = False
                    additional_log = False
                elif one_more.casefold() == "Yes".casefold():
                    wrong_input = False
                else:
                    print("Please type either yes or no.")

    def calculate_prompt(self):
        self.print_line()
        print("This is the calculate prompt")





if __name__ == "__main__":
    launch = User_Interface()