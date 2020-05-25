'''
 Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''
str= input('Enter a string: ')
n=int(input("enter the number of copies: "))
if n>=0:
    print(str*n)
else:
    print('negative integer not allowed.')