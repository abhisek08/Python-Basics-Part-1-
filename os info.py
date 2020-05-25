'''
Write a Python program to get OS name, platform and release information.
'''
import os
import platform
print(os.name)
print(platform.version())
print(platform.system())
print(platform.release())