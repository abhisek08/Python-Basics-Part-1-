'''
Write a Python program to determine whether variable is defined or not.
'''
try:
    a=20
    b
except BaseException as msg:
    print('variable is not defined:')
    print(msg)
    print(a)