#! python

import datetime, time

#it will show datetime basic oject related features
print(datetime.datetime.now())
dt = datetime.datetime(2018,10,31,11,10,49)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

#fromtimestamp 
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

#Arithmetic operations on datetime object
halloween2015 = datetime.datetime(2015,10,31,0,0,0)
newyear2016 = datetime.datetime(2016,1,1,0,0,0)
oct31_2015 = datetime.datetime(2015,10,31,0,0,0)

print(halloween2015 == oct31_2015) #True
print(halloween2015 > newyear2016) # False
print(newyear2016 > halloween2015) #True
print(newyear2016 != oct31_2015)   #True

#timedelta data type shows the duration of time rather a moment in time
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds)

#We can do addition and substraction using datetime.datetime and timedelta which will be time duration
dt1 = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print(dt1+thousandDays)

oct21st = datetime.datetime(2015,10,21,16,29,0)
aboutThirtyYears = datetime.timedelta(days=365*30)
print(oct21st - aboutThirtyYears)
print(oct21st - (2*aboutThirtyYears))

#Pausing your program until a specific date
halloween2016 = datetime.datetime(2019,10,31,0,0,0)
while datetime.datetime.now() > halloween2016:
	time.sleep(1)
	
#strftime function to convert dates to string
print('-------strftime function to convert dates to string--------')
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime("%B of '%y"))

#strptime function to convert string to dates
print('-------strptime function to convert string to dates--------')
print(datetime.datetime.strptime('October 21, 2015','%B %d, %Y'))
print(datetime.datetime.strptime("November of '63","%B of '%y"))


##############################################
'''
D:\Users\703224500\AppData\Local\Programs\Python\Python37-32>python.exe D:\Scrip
ts\datetimemoduleOperations.py
2018-11-01 10:46:58.724427
2018 10 31 11 10 49
1970-01-12 19:16:40
2018-11-01 10:46:58.724428
True
False
True
True
11 36548 0
<built-in method total_seconds of datetime.timedelta object at 0x006ED1E8>
2021-07-28 10:46:58.724427
1985-10-28 16:29:00
1955-11-05 16:29:00
-------strftime function to convert dates to string--------
2015/10/21 16:29:00
October of '15
-------strptime function to convert string to dates--------
2015-10-21 00:00:00
2063-11-01 00:00:00

D:\Users\703224500\AppData\Local\Programs\Python\Python37-32>
'''
##############################################
