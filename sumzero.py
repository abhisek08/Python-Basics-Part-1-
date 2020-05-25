'''
 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''
num1=int(input('enter the first number: '))
num2=int(input('enter the second number: '))
num3=int(input('enter the third number: '))
if num1==num2==0 or num1==num3==0 or num2==num3==0:
    print(0)
else:
    print(num1+num2+num3)