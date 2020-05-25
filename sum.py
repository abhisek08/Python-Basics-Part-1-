'''
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
'''
a=int(input('enter the first number: '))
b=int(input('enter the second number: '))
c=int(input('enter the third number: '))
if a==b==c:
    print(3*(a+b+c))
else:
    print(a+b+c)
