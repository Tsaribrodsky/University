# In python docs study for 'datetime' and 'time' modules regarding different features ,
# formats , methods , etc. Write some example programs on this matter.
from datetime import date, datetime
import math


class DateTime:
    def curentDay(self):
        today = date.today().strftime("%A %d %B %Y")
        print("Today is", today)

    def daysToBirthday(self):
        today = datetime.today()
        myBirthday = datetime(today.year, 7, 23)
        remeaningDays = abs(myBirthday - today)
        print("Days remaining until my birthday are", remeaningDays)

    def week_of_the_year(self):
        week = int(date.today().strftime("%W"))
        ordinal = lambda week: "%d%s" % (week,"tsnrhtdd"[(math.floor(week/10)%10!=1)*(week%10<4)*week%10::4])
        print("This week of the year is {}.".format(ordinal(week)))


day = DateTime()
day.curentDay()
day.daysToBirthday()
day.week_of_the_year()