'''
Write a Python program to concatenate all elements in a list into a string and return it.
'''
sample_list=[1,2,5,3,6]
str1=''
for a in sample_list:
    str1=str1+str(a)
print(str1)
print(type(str1))