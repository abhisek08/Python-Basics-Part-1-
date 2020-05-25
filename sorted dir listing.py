'''
Write a Python program to get a directory listing, sorted by creation date.
'''
import glob
files=glob.glob('*')
print(files)
import os
files.sort(key=os.path.getmtime)
for a in files:
    print(a)