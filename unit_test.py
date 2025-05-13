import classes as cl
import main 
import datetime as dt


myBudget_Calendar = cl.Budget_Calendar(2025)
print("Expenditure Test")
myBudget_Calendar.add_expenditure(dt.date(2025,4,22), cl.Expenditure("Spotify", 9.99, "Fixed", "Music"))
myBudget_Calendar.add_expenditure(dt.date(2025,4,22), cl.Expenditure("Spotify", 20.99, "Fixed", "Music"))
myBudget_Calendar.add_expenditure(dt.date(2025,4,23), cl.Expenditure("Spotify", 30.99, "Fixed", "Music"))
print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,4,22)))
print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,4,23)))
print(myBudget_Calendar.get_total_spending_amount_between_two_dates(dt.date(2025,4,22), dt.date(2025,4,23)))
myBudget_Calendar.add_fixed_expenditure(dt.date(2025,4,25), cl.Expenditure("Spotify", 9.99, "Fixed", "Music"), "monthly")
print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,4,25)))
print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,5,25)))
print(myBudget_Calendar.get_daily_spending_amount(dt.date(2025,12,25)))
print(myBudget_Calendar.get_total_spending_amount_between_two_dates(dt.date(2025,4,25), dt.date(2025,5,25)))

print("Income Test")
myBudget_Calendar.add_income(dt.date(2025,4,22), cl.Income("Pocket Money", 10.0, "Not Fixed"))
myBudget_Calendar.add_income(dt.date(2025,4,22), cl.Income("Pocket Money", 100.0, "Not Fixed"))
myBudget_Calendar.add_income(dt.date(2025,4,23), cl.Income("Pocket Money", 10.0, "Not Fixed"))
print(myBudget_Calendar.get_daily_income_amount(dt.date(2025,4,22)))
print(myBudget_Calendar.get_daily_income_amount(dt.date(2025,4,23)))
print(myBudget_Calendar.get_total_income_amount_between_two_dates(dt.date(2025,4,22), dt.date(2025,4,22)))
myBudget_Calendar.add_fixed_income(dt.date(2025,4,25), cl.Income("Pocket Money", 10.0, "Fixed"), "monthly")
print(myBudget_Calendar.get_daily_income_amount(dt.date(2025,4,25)))
print(myBudget_Calendar.get_daily_income_amount(dt.date(2025,5,25)))
print(myBudget_Calendar.get_daily_income_amount(dt.date(2025,12,25)))
print(myBudget_Calendar.get_total_income_amount_between_two_dates(dt.date(2025,4,25), dt.date(2025,5,25)))

print("Fund Test")
print(myBudget_Calendar.get_daily_change_in_fund(dt.date(2025,4,23)))
print(myBudget_Calendar.get_total_fund_left_between_two_dates(dt.date(2025,4,22), dt.date(2025,4,23)))

print("calculate test")
print(myBudget_Calendar.get_total_spending_amount_between_two_dates(dt.date(2025,4,22), dt.date(2025,5,25)))
print(myBudget_Calendar.get_total_income_amount_between_two_dates(dt.date(2025,4,22), dt.date(2025,5,25)))
print(abs((dt.date(2025,5,25) - dt.date(2025,4,22)).days) + 1)
print(myBudget_Calendar.get_recommended_daily_budget(dt.date(2025,4,22), dt.date(2025,5,25)))
