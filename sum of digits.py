'''
Write a Python program to calculate the sum of the digits in an integer
'''
num=int(input('enter a number: '))
s=0
while num!=0:
    r=int(num%10)
    num=num/10
    s=s+r
print(s)