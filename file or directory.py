'''
Write a Python program to check whether a file path is a file or a directory
'''
import os
print(os.path.isfile('abc.txt'))
print(os.path.isdir('abc.txt'))