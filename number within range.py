'''
Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''
num=int(input('Enter a number: '))
if num>=900 and num<=1000:
    print('number is within 100 of 1000')
elif num>=1900 and num<=2000:
    print('number is within 100 of 2000')