import datetime

year = int(input("Please enter a year: "))
month = int(input("Please enter a month (numerical): "))
if month > 12:
    month = int(input("Not a valid month... Please enter a valid numerical month (1-12): "))
day = int(input("Please enter a day: "))
if day > 31:
    day = int(input("Not a valid day... Please enter a valid numerical day: "))

if day == 31 and month != (1,3,5,7,8,9,10,12):
    day = int(input("Not a valid day... Please enter a valid numerical day: "))

if day == 30 and month == 2:
    day = int(input("Not a valid day... Please enter a valid numerical day: "))

if day == 29 and month == 2:
    day = int(input("Not a valid day... Please enter a valid numerical day: "))

today = datetime.date.today()
future = datetime.date(year, month, day)
diff = future - today
print("There are ", diff.days, "days until", month,"/",day,"/",year)