import calendar
date = list(map(int, input().split()))
print(list(calendar.day_name)[calendar.weekday(date[2], date[0], date[1])].upper())