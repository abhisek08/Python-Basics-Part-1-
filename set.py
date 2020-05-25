'''
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
set3=set()
for a in color_list_1:
    if a not in color_list_2:
      set3.add(a)
print(set3)

