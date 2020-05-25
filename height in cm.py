'''
Write a Python program to convert height (in feet and inches) to centimeters.
'''
height=int(input('enter your height in feet: '))
inches=int(input('enter inches: '))
print('your height is: {}feet{}inches'.format(height,inches))
print('your height in centimeteres is: ',height*12*2.54+inches*2.54)