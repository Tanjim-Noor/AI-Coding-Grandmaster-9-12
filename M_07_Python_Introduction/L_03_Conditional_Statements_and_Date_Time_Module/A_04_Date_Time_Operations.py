"""
Activity 4
Title: Date Time Operations
Short description:
Create a program to display today's date, time, hour, mins, second, and calendar year.
"""

import datetime
import calendar

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print ("Time now at greenwich meridian is : ", end = "")
print (current_time)

# print calendar of year 2021 (example year in screenshot)
print("\n", calendar.calendar(2021))
