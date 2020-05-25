'''
 Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
'''
pressure= int(input('enter pressure in kilopascals: '))
print('pressure in psi is: ',pressure*0.145038)
print('pressure in mmHg is: ',pressure*7.50062)
print('pressure in atm is: ',pressure*0.00986923)