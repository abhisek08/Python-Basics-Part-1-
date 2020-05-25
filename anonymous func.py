'''
Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
'''
lst=[10,20,30,40,50,60]
a=list(filter(lambda a:a%15==0,lst))
print(a)