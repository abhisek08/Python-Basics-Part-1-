'''
Write a Python program to calculate the time runs (difference between start and current time) of a program.
'''
import time
s_t=time.time()
a=10
time.sleep(1)
b=20
time.sleep(1)
c=a+b
time.sleep(1)
print(c)
c_t=time.time()
time_run=c_t-s_t
print(time_run)