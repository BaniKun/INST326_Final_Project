# File for main function to run the app
import classes
import pickle
import datetime as dt

class User_Interface:
    """A class for user interface where the user get to interact with the budget calendar

    Attributes:
        year (int): The year the calendar will be set
        calendar (budget calendar object): the budget calendar object where the user can interact with
    """
    def __init__(self):
        """Initializes the user interface

        Side Effects:
            Loads a saved calendar if user says yes or creates a new one based on the year input by the user and starts the main menu
        """
        self.print_line()
        print("Welcome to your Budget Calendar!")

        wrong_input = True # Checks for correct input from the user on the first prompt
        while wrong_input: # Repeats as long as the user puts in an unaccepted input
            self.print_line() 
            print("Would you like to load a existing calendar? (Yes/No)") # First prompt
            user_input = input()
            if user_input.casefold() == "Yes".casefold(): # Case where the user wants to load a calendar
                self.load_calendar() # Calls for method that loads in a pre-saved calendar and saves it to the calendar attribute
                wrong_input = False # Breaks free of the first while loop
            elif user_input.casefold() == "No".casefold(): # Case where the user wants to create a new calendar
                wrong_second_input = True # Checks for correct input from the user on the second prompt
                while wrong_second_input: # Repeats as long as the user puts in an unaccepted input 
                    self.print_line()
                    print("What year would you like to make a calendar for?") # Second prompt
                    try: 
                        self.year = int(input()) # Saves the year of the calendar as an attribute
                        self.calendar = classes.Budget_Calendar(self.year) # Creates a new budget calendar object and saves it to the calendar attribute
                        wrong_second_input = False # Breaks free of the second while loop
                    except: # Catches any instance where the user does not input accepted year for the second prompt
                        self.print_line()
                        print("Please input the year in numbers.")
                    
                    wrong_input = False # Breaks free of the first while loop
            else: # Case where the user inputs an unaccepted input for the first prompt
                self.print_line()
                print("Please enter either yes or no.")
        
        self.main_menu() # Calls the main menu method 

    def print_line(self):
        """A method that prints out a dash line, for our sanity

        Side Effect:
            Prints out a line with 60 dashes
        """
        print("------------------------------------------------------------")        
    
    def save_calendar(self):
        """A method that saves the calendar attribute as a pickle file so that user can load it up later

        Side Effect:
            Calls the main menu once the calendar is saved
        """
        self.print_line()
        filename = input("Enter the filename you want to save your calendar as: ")
        filename += ".pkl"
        with open(filename, 'wb') as file:
            pickle.dump(self.calendar, file)
        
        self.main_menu()

    def load_calendar(self):
        """A method that loads a pre-saved calendar with the filename that user inputs 
        """
        wrong_input = True # Checks for correct input from the user 
        while wrong_input: # Repeats as long as the user puts in an unaccepted input
            self.print_line()
            filename = input("Enter the filename of the calendar that you want to open: ")
            try: # Tries to open a pickle file with the name that the user inputs
                with open(filename, 'rb') as file:
                    self.calendar = pickle.load(file)
                print("Calendar loaded successfully.")
                wrong_input = False # Breaks free from the while loop
            except: # Cathces any instance where the filename user input is incorrect
                print("Please enter the correct filename.")

        

    def main_menu(self):
        """A method that prompts the main menu to the user

        Side Effect:
            Prompts the user between adding income or expense, or run a calculation on the Calendar.
        """
        wrong_input = True # Checks for correct input from the user 

        while wrong_input: # Repeats as long as the user puts in an unaccepted input
            self.print_line()
            print("What would you like to do?\n - Add Income\n - Add Expense\n - Calculate Daily Budget\n - Check\n - Save Calendar\n - Quit") # Prints out all the options / Add the option here if you add another option underneath / Quit should always be the last option
            user_input = input()
            if user_input.casefold() == "Add Income".casefold(): # If the user chooses to add income to the calendar
                self.add_income_prompt()
                wrong_input = False
            elif user_input.casefold() == "Add Expense".casefold(): # If the user chooses to add expense to the calendar
                self.add_expense_prompt()
                wrong_input = False
            elif user_input.casefold() == "Calculate Daily Budget".casefold(): # If the user chooses to calculate daily recommended budget on the calendar
                self.calculate_prompt()
                wrong_input = False
            elif user_input.casefold() == "Check".casefold(): # If the user chooses to check funds on the calendar
                self.check_prompt()
                wrong_input = False
            elif user_input.casefold() == "Save Calendar".casefold(): # If the user chooses to save the calendar
                self.save_calendar()
                wrong_input = False
            elif user_input.casefold() == "Quit".casefold(): # If the user chooses to quit the program
                quit()
            else: # If the user input does not match any of the options
                self.print_line()
                print("Please enter correctly.")

    
    def add_expense_prompt(self):
        """Method that adds an expense object to the calendar attribute

        Side Effects:
            Depending on the user input, it adds either a single or fixed expense object to the calendar.
            Allows the user to input additional expenses if the user chooses to.
            Calls the main menu after it's finished.
        """
        additional_log = True # Checks if the user wishes to input additional expenses
        while additional_log: 
            self.print_line()
            wrong_input = True # Fail-safe for first prompt
            while wrong_input:
                print("Would you like to add a single expense or a fixed expense? (single/fixed)") # First prompt
                user_input = input()
                if user_input.casefold() == "single".casefold(): # Case where the user chooses to log a single expense
                    description = input("Describe your expense. (i.e. Mcdonalds)\n")
                    wrong_date_input = True # Checks for wrong input for the date
                    while wrong_date_input:
                        try: # Tries to make a date object based on the user's input
                            date_input = input("When was this expense made?(Input in MM/DD/YYYY format)\n")
                            date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                            wrong_date_input = False # Breaks free from the while loop if the input is correct
                        except: # Catches any instance where the user input couldn't be made into a date object
                            print("Please input the date correctly.")

                    amount = input("How much did you spend?\n")
                    expense_type = "not fixed"
                    category = input("What category does it fall into? (i.e. Food, Hobby, etc)\n")

                    new_expense = classes.Expenditure(description, amount, expense_type, category) # Makes an expense object based on user input

                    self.calendar.add_expenditure(date, new_expense) # Adds the expense object to the calendar attribute
                    wrong_input = False # Breaks free of the while loop for first prompt
                
                elif user_input.casefold() == "fixed".casefold(): # Case where the user chooses to log a fixed expense (or a subscription)
                    description = input("Describe your expense. (i.e. Mcdonalds)\n")

                    wrong_date_input = True # Checks for wrong input for the date
                    while wrong_date_input:
                        try: # Tries to make a date object based on the user's input
                            date_input = input("When was this expense made for the first time? (Input in MM/DD/YYYY format)\n")
                            date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                            wrong_date_input = False # Breaks free from the while loop if the input is correct
                        except: # Catches any instance where the user input couldn't be made into a date object
                            print("Please input the date correctly.")

                    amount = input("How much is each payment?\n")

                    wrong_frequence_input = True # Checks wrong input for second prompt
                    while wrong_frequence_input:
                        frequence = input("How often do you make this payment? (monthly/yearly)\n") # Second prompt
                        if frequence.casefold() == "yearly".casefold() or "monthly".casefold(): 
                            expense_type = frequence
                            wrong_frequence_input = False # Breaks free of the while loop that checks for the second prompt
                        else: # Case where the user input is incorrect
                            print("Please input the frequence correctly.")

                    category = input("What category does it fall into? (i.e. Food, Hobby, etc)\n")

                    new_expense = classes.Expenditure(description, amount, expense_type, category) # Creates a expense object based on user input

                    self.calendar.add_fixed_expenditure(date, new_expense) # Adds a fixed expense to the calendar attribute
                    wrong_input = False # Breaks free from the while loop that checks for the first prompt
                
                else: # Case where the user puts in unaccepted input for the first prompt
                    print("Please type in either single or fixed.")
            
            wrong_input = True # Chacks for the wrong input for the third prompt
            while wrong_input:
                one_more = input("Would you like to add another expense? (Yes/No)\n") # Third prompt
                if one_more.casefold() == "No".casefold(): # Case where the user chooses not to log additional expenses
                    wrong_input = False # Breaking free from the while loop that checks for the third prompt
                    additional_log = False # Breaking free from the while loop that checks for additional logs
                elif one_more.casefold() == "Yes".casefold(): # Case where the user chooses to log additional expenses
                    wrong_input = False # Breaking free from the while loop that checks for the third prompt
                else: # Case where the user puts in wrong input for the third prompt
                    print("Please type either yes or no.")
        
        self.main_menu() # Calls the main menu method after breaking free from the while loop that checks for additional logs


    def add_income_prompt(self):
        """Method that adds an income object to the calendar attribute

        Side Effects:
            Depending on the user input, it adds either a single or fixed income object to the calendar.
            Allows the user to input additional incomes if the user chooses to.
            Calls the main menu after it's finished.
        """
        additional_log = True
        while additional_log:
            self.print_line()
            wrong_input = True
            while wrong_input:
                print("Would you like to add a single income or a fixed income? (single/fixed)")
                user_input = input()
                if user_input.casefold() == "single".casefold():
                    description = input("Describe your income. (i.e. Allowance)\n")
                    wrong_date_input = True
                    while wrong_date_input:
                        try:
                            date_input = input("When was this income paid? (Input in MM/DD/YYYY format)\n")
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
                            date_input = input("When was this income paid for the first time?(Input in MM/DD/YYYY format)\n")
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
                one_more = input("Would you like to add another income? (Yes/No)\n")
                if one_more.casefold() == "No".casefold():
                    wrong_input = False
                    additional_log = False
                elif one_more.casefold() == "Yes".casefold():
                    wrong_input = False
                else:
                    print("Please type either yes or no.")
        
        self.main_menu()

    def calculate_prompt(self):
        """Method that calculates the recommended daily budget for each day between two dates that the user chooses

        Side Effect:
            Prints out the result message.
            User can calculate it again for different time period if the user chooses to.
            Calls the main menu method once it's finished
        """
        additional_log = True
        while additional_log:
            self.print_line()
            wrong_date_input = True
            while wrong_date_input:
                try:
                    date_input = input("What is the starting date you want to calculate recommended daily budget for? (Input in MM/DD/YYYY format)\n")
                    start_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                    wrong_date_input = False
                except:
                    print("Please input the date correctly.")

            wrong_date_input = True
            while wrong_date_input:
                try:
                    date_input = input("What is the ending date you want to calculate recommended daily budget for?(Input in MM/DD/YYYY format)\n")
                    end_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                    wrong_date_input = False
                except:
                    print("Please input the date correctly.")
            
            total_fund = self.calendar.get_total_fund_left_between_two_dates(dt.date(self.year,1,1), end_date)
            num_of_days = abs((end_date - start_date).days) + 1
            recommended_budget = self.calendar.get_recommended_daily_budget(start_date, end_date)

            self.print_line()
            print(f"Report\nDate: {start_date} ~ {end_date}\nToTal Fund Available: {total_fund}\nNumber of days between two dates: {num_of_days}\nRecommended Daily Budget: {recommended_budget}")

            wrong_input = True
            while wrong_input:
                one_more = input("Would you like to calculate daily recommended budget for other dates? (Yes/No)\n")
                if one_more.casefold() == "No".casefold():
                    wrong_input = False
                    additional_log = False
                elif one_more.casefold() == "Yes".casefold():
                    wrong_input = False
                else:
                    print("Please type either yes or no.")  

        self.main_menu()   
    
    def check_prompt(self):
        """Method that checks for incomes, expenses, or change in fund depending on the user input

        Side Effect:
            Prints out the results.
            Allows user to repeat the process if the user chooses to.
            Calls the main menu method once it finishes.
        """
        self.print_line()
        additional_log = True
        while additional_log:
            wrong_input = True

            while wrong_input:
                self.print_line()
                print("What would you like to do?\n - Check Expense\n - Check Income\n - Check Change in Funds")
                user_input = input()
                if user_input.casefold() == "check expense".casefold(): # Case where user chooses to check for expense
                    self.print_line()

                    wrong_second_input = True
                    while wrong_second_input:
                        print("Would you like to check expense on a single date or between two dates? (Single/Two Dates)")
                        user_second_input = input()
                        if user_second_input.casefold() == "Single".casefold(): # Case where user chooses to check for expense on a single date
                            self.print_line()

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What date do you wish to check total expense for? (Input in MM/DD/YYYY format)\n")
                                    check_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")
                            
                            total_spent = self.calendar.get_daily_spending_amount(check_date)
                            print(f"On {check_date}, you've spent total of ${total_spent}.")

                            wrong_second_input = False
                        elif user_second_input.casefold() == "Two Dates".casefold(): # Case where user chooses to check for expense between two dates
                            self.print_line()

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What is the starting date you want to check total expense for? (Input in MM/DD/YYYY format)\n")
                                    start_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What is the ending date you want to check total expense for? (Input in MM/DD/YYYY format)\n")
                                    end_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")

                            total_spent = self.calendar.get_total_spending_amount_between_two_dates(start_date, end_date)
                            print(f"Your total spending between {start_date} and {end_date} is ${total_spent}.")

                            wrong_second_input = False
                        else: # Case where the user puts in wrong input
                            print("Please enter correctly.")

                    wrong_input = False
                elif user_input.casefold() == "Check Income".casefold(): # Case where the user chooses to check for income
                    self.print_line()

                    wrong_second_input = True
                    while wrong_second_input:
                        print("Would you like to check income on a single date or between two dates? (Single/Two Dates)")
                        user_second_input = input()
                        if user_second_input.casefold() == "Single".casefold(): # Case where the user chooses to check for income on a single date
                            self.print_line()

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What date do you with to check total income for? (Input in MM/DD/YYYY format)\n")
                                    check_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")
                            
                            total_gained = self.calendar.get_daily_income_amount(check_date)
                            print(f"On {check_date}, you've gained total of ${total_gained}.")

                            wrong_second_input = False
                        elif user_second_input.casefold() == "Two Dates".casefold(): # Case where the suer chooses to check for income between two dates
                            self.print_line()

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What is the starting date you want to check total income for? (Input in MM/DD/YYYY format)\n")
                                    start_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What is the ending date you want to check total income for? (Input in MM/DD/YYYY format)\n")
                                    end_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")

                            total_gained = self.calendar.get_total_income_amount_between_two_dates(start_date, end_date)
                            print(f"Your total income between {start_date} and {end_date} is ${total_gained}.")

                            wrong_second_input = False
                        else: # Case where the user inputs incorrectly
                            print("Please enter correctly.")
                    
                    wrong_input = False
                
                elif user_input.casefold() == "Check Total change in funds".casefold(): # Case where the user chooses to check for total change in fund
                    self.print_line()

                    wrong_second_input = True
                    while wrong_second_input:
                        print("Would you like to check total change in funds on a single date or between two dates? (Single/Two Dates)")
                        user_second_input = input()
                        if user_second_input.casefold() == "Single".casefold(): # Case where the user chooses to check for total change in fund on a single date
                            self.print_line()

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What date do you with to check total change in funds for? (Input in MM/DD/YYYY format)\n")
                                    check_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")
                            
                            total_change = self.calendar.get_daily_change_in_fund(check_date)
                            print(f"On {check_date}, you've gained total of ${total_change}.")

                            wrong_second_input = False
                        elif user_second_input.casefold() == "Two Dates".casefold(): # Case where the user chooses to check for total change in fund between two dates
                            self.print_line()

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What is the starting date you want to check total change in funds for? (Input in MM/DD/YYYY format)\n")
                                    start_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")

                            wrong_date_input = True
                            while wrong_date_input:
                                try:
                                    date_input = input("What is the ending date you want to check total change in funds for? (Input in MM/DD/YYYY format)\n")
                                    end_date = dt.date(int(date_input.split("/")[2]), int(date_input.split("/")[0]), int(date_input.split("/")[1]))
                                    wrong_date_input = False
                                except:
                                    print("Please input the date correctly.")

                            total_change = self.calendar.get_total_fund_left_between_two_dates(start_date, end_date)
                            print(f"Your total change in funds between {start_date} and {end_date} is ${total_change}.")

                            wrong_second_input = False
                        else: # Case where the user puts in wrong input
                            print("Please enter correctly.")
                    
                    wrong_input = False

                else: # If the user input does not match any of the options
                    self.print_line()
                    print("Please enter correctly.")
        
            wrong_input = True
            while wrong_input:
                one_more = input("Would you like to check for more dates? (Yes/No)\n")
                if one_more.casefold() == "No".casefold():
                    wrong_input = False
                    additional_log = False
                elif one_more.casefold() == "Yes".casefold():
                    wrong_input = False
                else:
                    print("Please type either yes or no.") 
        
        self.main_menu()

if __name__ == "__main__":
    launch = User_Interface()