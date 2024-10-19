time = input("please write date and time using timezone (format: year-month-dayThour:minutes:seconds:mseconds(6 digit)timezone(do not forget to write + sign)). - ")

year = time[0:4]
month = time[5:7]
day = time[8:10]
desh = time[4:5]

if int(time[11:13]) > 12:
    hour = int(time[11:13])-12
else:
    hour = int(time[11:13])

minutes_and_seconds = time[13:19]
timezone = time[26:27]+time[28:29]

print(day, desh, month, desh, year+ " "  +str(hour), minutes_and_seconds+ " " +timezone, sep='')

