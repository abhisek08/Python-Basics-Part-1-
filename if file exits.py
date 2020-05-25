'''
Write a Python program to check whether a file exists.
'''
import os.path
open('abc.txt',mode='w')
print(os.path.isfile('abc.txt'))