'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''
n=int(input("Enter the value of n :"))
base_10= n*10+n
base_100=n*100+n*10+n
print('Expected Result :',n+base_10+base_100)