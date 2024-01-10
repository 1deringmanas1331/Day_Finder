# Imports Datetime Library for finding the date of the day
import datetime
# Define a function to check the day
def predict_day_of_week():
    while True:
        try:
            # Asks the user for the date
            year = int(input("Enter the year (e.g., 2023): "))
            month = int(input("Enter the month (1-12): "))
            day = int(input("Enter the day (1-31): "))
            input_date = datetime.date(year, month, day)
            
            # Finds the day for the given date
            day_of_week = input_date.strftime("%A")
            print(f"The day of the week for {input_date} is {day_of_week}.")
            break
        except ValueError:
            print("Invalid date input. Please enter a valid date.")

if __name__ == "__main__":
    predict_day_of_week()
