'''
Write a Python program to filter the positive numbers from a list.
'''
lst=[1,-1,2,-2,3,-3,4,-5]
a=list(filter(lambda b:b>0,lst))
print(a)