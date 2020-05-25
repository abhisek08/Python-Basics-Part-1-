'''
Write a Python program to input a number, if it is not a number generate an error message.
'''
try:
    a=int(input('enter a num: '))
    print(a)
except ValueError as msg:
    print('It is not a number')
    print(msg)