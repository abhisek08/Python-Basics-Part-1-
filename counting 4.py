'''
Write a Python program to count the number 4 in a given list.
'''
num=input("Enter the number : ")
a=list(num)
count=0
for b in a:
    if b=='4':
        count+=1
print(count)

