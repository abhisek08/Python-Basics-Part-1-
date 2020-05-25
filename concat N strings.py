'''
Write a Python program to concatenate N strings.
'''
n=int(input('enter the number of string: '))
c=''
for a in range(1,n+1):
    b=input()
    c=c+b
print(c)