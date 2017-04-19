import calendar

month, day, year = map(int, input().split(' '))

print(str.upper(calendar.day_name[calendar.weekday(year, month, day)]))
