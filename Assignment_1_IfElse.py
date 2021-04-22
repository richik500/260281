date = input()
date = date.split('-')
year = int(date[2])
month = int(date[1])
day = int(date[0])
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
   leap_year = False
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
       month_length = 29
    else:
        month_length = 28
else:
    month_length = 30
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
       month += 1
print("The next  date is [dd-mm-yyyy] %d-%d-%d." % (day, month, year))