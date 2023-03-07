import calendar

date = list(map(int,input().split()))
m,d,y = date
print(calendar.day_name[calendar.weekday(y,m,d)][:].upper())
  