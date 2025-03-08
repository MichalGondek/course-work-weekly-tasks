# Write a Program that Outputs Whether or Not Today is a Weekday
# Author: Michal Gondek

from datetime import datetime


# Get the current day of the week as an integer (0=Monday, 6=Sunday)
today_weekday = datetime.today().weekday()

# Check if today is a weekday (Monday=0 to Friday=4)
if today_weekday < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

