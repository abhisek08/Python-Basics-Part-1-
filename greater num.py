'''
Write a Python program to test whether all numbers of a list is greater than a certain number
'''
num=int(input('enter a reference number: '))
lst=[20,30,10,50,35,48]
for a in lst:
    if a>num:
        print('{} is greater than {}'.format(a,num))
    else:
        print('{} is less than {}'.format(a, num))