'''
Write a Python program to check if a number is positive, negative or zero.
'''
num=int(input('enter a num: '))
if num==0:
    print(num,'is zero')
elif num>0:
    print(num,'is +ve')
else:
    print(num,'is -ve')