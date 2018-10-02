import datetime

print("Tell us when you were born: ")
year = int(input("Year [YYYY]: "))
month = int(input("Month [MM]: "))
day = int(input("Day [DD]: "))

# birthday = datetime.datetime(year, month, day)

date1 = now()
# date2 = datetime.datetime(original_date.year, original_date.month, original_date.day)
dt = date1 - birthday
days = int(dt.total_seconds() / 60 / 60 / 24)
print(days)
