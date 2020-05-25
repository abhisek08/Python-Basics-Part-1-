'''
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
'''
x1=int(input("enter x1: "))
y1=int(input("enter y1: "))
x2=int(input("enter x2: "))
y2=int(input("enter y2: "))
distance=((x2-x1)**2 + (y2-y1)**2)**0.5
print("distance is:",distance.__round__(2))