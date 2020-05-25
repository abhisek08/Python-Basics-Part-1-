'''
 Write a Python program to check whether a specified value is contained in a group of values.
'''
sample_list=[3,23,5,6,7,4,6,4,1,5676,32]
value=int(input('enter a value: '))
if value in sample_list:
    print(value,'is present in the group')
else:
    print(value, 'is  not present in the group')