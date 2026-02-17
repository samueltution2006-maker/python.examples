import _datetime

x = _datetime.datetime.now()  #08-07-2021 08:02:10

print("X as is", x)
print(x.year)
print(x.month)
print(x.day)

print("Weekday's no and Day of month", x.strftime("%w"), x.strftime("%d"))
print("Month short ",  x.strftime("%b"))
print("Month full ",  x.strftime("%B"))
print("Month as number", x.strftime("%m"))
print("Day number of year", x.strftime("%j"))

print("Week number of year - Sunday", x.strftime("%U"))
print("Week number of year - Monday", x.strftime("%W"))

print("Year, month, day full version", x.strftime("%Y %B %A"))
print("Year, month, day short version", x.strftime("%y %b %a"))

print("Hours, minutes and seconds - 24 hours", x.strftime("%H %M %S %p"))
print("Hours, minutes and seconds - 12 hours", x.strftime("%I %M %S %p"))