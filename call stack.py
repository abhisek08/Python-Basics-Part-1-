'''
 Write a Python program to print the current call stack.
'''
import traceback
def f1():
    print(f2())
def f2():
    traceback.print_stack()
f1()