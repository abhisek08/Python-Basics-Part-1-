'''
 Write a Python program to sort three integers without using conditional statements and loops.
'''
print('enter 3 numbers:')
lst=[]
for a in range(3):
    lst.append(int(input()))
print(lst)
lst.sort()
print('sorted list: ',lst)
