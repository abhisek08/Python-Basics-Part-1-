'''
Write a Python program to sum of all counts in a collections?
'''
import collections
lst=[2,2,2,1,1,5,5,6,6,7]
print(sum(collections.Counter(lst).values()))
