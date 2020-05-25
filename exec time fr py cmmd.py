'''
 Write a program to get execution time for a Python method.
'''
import time
def summation(n):
    start_time=time.time()
    s=0
    for i in range(0,n):
        s=s+i
    end_time=time.time()
    return s,end_time-start_time
n=5
print(summation(5))