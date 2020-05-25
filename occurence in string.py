'''
Write a Python program to count the number occurrence of a specific character in a string.
'''
string=input('enter an arbitary string: ')
character=input('enter a specific character: ')
count=0
for a in string:
    if a==character:
        count+=1
print(character,'occured',count,'times')
print(string.count(character))