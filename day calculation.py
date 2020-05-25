'''
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
import datetime
date1=datetime.date(2020,2,26)
date2=datetime.date(2000,1,26)
date3=date1-date2
print(date3)