'''
Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
'''
import sys
print('name of script: ',sys.argv[0])
print('number of arguments: ',len(sys.argv))
print('name of arguments: ',sys.argv)