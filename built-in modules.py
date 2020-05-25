'''
Write a Python program to find the available built-in modules.

import sys
print(sys.builtin_module_names)
'''
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))