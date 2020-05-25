'''
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
'''
name=input('Enter your name: ')
lst=[]
for a in name.split():
    lst.append(a)
for a in lst[::-1]:
    print(a,end=' ')