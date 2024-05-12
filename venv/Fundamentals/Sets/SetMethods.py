'''
Define two sets
'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

'''
Adding an item to a set using add() method
'''
set1.add(6)
print("Set after adding 6 using add():", set1)

'''
Removing an item from a set using remove() method
'''
set1.remove(2)
print("Set after removing 2 using remove():", set1)

'''
Checking if an item is in a set using the in keyword
'''
if 3 in set1:
    print("3 is in set1")
else:
    print("3 is not in set1")

'''
Obtaining the length of a set using len() method
'''
length_set1 = len(set1)
print("Length of set1:", length_set1)

'''
Copying a set using copy() method
'''
set1_copy = set1.copy()
print("Copy of set1:", set1_copy)

# Clearing all items from a set using clear() method
set1.clear()
print("Set1 after clearing all items:", set1)

'''
Checking for disjoint sets using isdisjoint() method
'''
if set1_copy.isdisjoint(set2):
    print("set1_copy and set2 have no common elements")
else:
    print("set1_copy and set2 have common elements")

'''
Finding the intersection of sets using intersection() method or &
'''
intersection_set = set1_copy.intersection(set2)
print("Intersection of set1_copy and set2:", intersection_set)

'''
Finding the union of sets using union() method or |
'''
union_set = set1_copy.union(set2)
print("Union of set1_copy and set2:", union_set)

'''
 Finding the difference between sets using difference() method or -
'''
difference_set = set1_copy.difference(set2)
print("Difference between set1_copy and set2:", difference_set)

'''
Finding the symmetric difference between sets using symmetric_difference() method or ^
'''
symmetric_difference_set = set1_copy.symmetric_difference(set2)
print("Symmetric difference between set1_copy and set2:", symmetric_difference_set)
