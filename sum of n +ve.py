'''
Write a python program to find the sum of the first n positive integers
'''
n=int(input('Enter the limit: '))
s=0
for i in range(0,n+1):
    s=s+i
print('sum is: ',s)
