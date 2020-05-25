'''
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
'''
num1=int(input('Enter the 1st number: '))
num2=int(input('Enter the 2nd number: '))
lst1=[]
lst2=[]
lst3=[]
for a in range(1,num1+1):
    if num1%a==0:
        lst1.append(a)
for a in range(1,num2+1):
    if num2%a==0:
        lst2.append(a)
for a in lst1:
    if a in lst2:
        lst3.append(a)
lst3.sort()
print(lst3[-1])