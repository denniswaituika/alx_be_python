from datetime import timedelta
from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    print('Current date and time: ', current_date.strftime("%Y-%m-%d %H:%M:%S" ))

def calculate_future_date():
    number_of_days = int(input("enter a number of days"))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print("Future date: ", future_date.strftime("%Y-%m-%d" ))


display_current_datetime()
calculate_future_date()