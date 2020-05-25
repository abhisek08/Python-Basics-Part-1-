'''
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
'''
num=float(input('enter a number'))
if num>17:
    diff=num-17
    print(abs(diff)*2)
else:
    print(17-num)
