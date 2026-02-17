import _datetime
from _datetime import date
from _datetime import time
from _datetime import timedelta

 
my_date = date(1996, 12, 11)    #date class - __init__(3 params)
print("Date passed as argument is", my_date)
print(my_date.day)
print(my_date.month)
print(my_date.year)

today = date.today()
print("Today's date is", today)
print("Date components", today.year, today.month, today.day)

my_time = time(12, 24, 36)
print("\nTime", my_time)
print("Time components", my_time.hour, my_time.minute, my_time.second)

time_now = _datetime.datetime.now()
print ("initial_date", str(time_now))
   
new_time = time_now + timedelta(days = 2)
print ("new_time", str(new_time))

new_time1 = time_now + timedelta(hours = 2)
print ("new_time", str(new_time1))
