'''
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
'''
filename=input('Enter a file name: ')
print('filename :',filename)
lst=[]
for a in filename.split('.'):
    lst.append(a)
print("Output :",lst[-1])