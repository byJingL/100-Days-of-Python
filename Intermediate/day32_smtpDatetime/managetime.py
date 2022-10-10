import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(type(now), type(year), year, month)
print(day_of_week)

# hour, minute, second have default value
date_of_birth = dt.datetime(year=1997, month=3, day=4)
print(date_of_birth)
