# Write a program that prints the next 20 leap years.

import calendar
import datetime

count = 0
year = datetime.date.today().strftime("%Y")
print("Today is", year)
intYear = int(year)
yearCount = intYear + 20 + 1

for y in range(intYear, yearCount):
    if calendar.isleap(y):
        print("{} is a leap year." .format(y))

