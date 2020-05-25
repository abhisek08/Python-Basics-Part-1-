'''
Write a python program to call an external command in Python.
'''
import subprocess
print(subprocess.call(['ls','-1']))