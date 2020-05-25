'''
Write a Python program to convert seconds to day, hour, minutes and seconds.
'''
seconds=int(input('enter time in seconds: '))
minutes=int(seconds/60)
hour=int(minutes/60)
day=int(hour/24)
print('entered time in seconds is: ',seconds)
print('entered time in minute is: ',minutes)
print('entered time in hours is: ',hour)
print('entered time in day is: ',day)