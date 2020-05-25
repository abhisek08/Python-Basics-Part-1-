'''
Write a Python program to retrieve file properties.
'''
import os
import time
print(__file__)
print(os.path.getsize(__file__))
print(time.ctime(os.path.getmtime(__file__)))
print(time.ctime(os.path.getatime(__file__)))
print(time.ctime(os.path.getctime(__file__)))
