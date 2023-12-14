import datetime

start = datetime.date(2023, 1, 6)
period = datetime.timedelta(days = 7)
end = start + period

print(start)
print(end)

date1 = datetime.date(2023, 1, 7)
date2 = datetime.date(2023, 1, 5)

if start < date1 and end > date1:
    print(f"{date1} is within the time period")