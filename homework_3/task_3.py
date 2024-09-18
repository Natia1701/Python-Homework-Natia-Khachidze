year = int(input ("enter your year of birth- "))
month = int(input ("enter your month of birth- "))
day = int(input ("enter your day of birth- "))

import datetime

date = datetime.date (year, month, day)
day_of_the_week = date.strftime("%A")

print (day_of_the_week)