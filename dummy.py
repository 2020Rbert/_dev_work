import datetime
now = datetime.datetime.now()
new_year = now.month ==11 and now.day == 22
print(new_year)
print(f"Datum heute: {now.day}.{now.month}.{now.year}")