'''
Write a Python program to compute the product of a list of integers (without using for loop).
'''
import functools
lst=[1,2,3,4,5,6,7,8]
a=functools.reduce(lambda a,b:a*b,lst)
print(a)