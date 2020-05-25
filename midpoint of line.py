'''
Write a Python program to calculate midpoints of a line.
'''
print('enter coordinates of a: ')
x1=int(input('x1= '))
y1=int(input('y1= '))
tpl=[x1,y1]
print('(x1,y1)=',tuple(tpl))
print('enter coordinates of b: ')
x2=int(input('x2= '))
y2=int(input('y2= '))
tpl1=[x2,y2]
print('(x1,y1)=',tuple(tpl1))
mid=[(x2-x1)/2,(y2-y1)/2]
print('midpoint=',tuple(mid))