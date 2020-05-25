'''
Write a Python program to prove that two string variables of same value point same memory location.
'''
a='str'
print(id(a))
b=a
print(id(b))