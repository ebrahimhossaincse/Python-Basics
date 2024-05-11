'''
Joining Lists Examples
'''

# Lists to join
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

'''
Method 1: Using the '+' operator
'''
print("Method 1: Using the '+' operator")
result1 = list1 + list2
print("Result:", result1)

'''
Method 2: Using the extend() method
'''
print("\nMethod 2: Using the extend() method")
list1.extend(list2)
print("Result:", list1)

'''
Method 3: Using list comprehension
'''
print("\nMethod 3: Using list comprehension")
result3 = [item for sublist in [list1, list2] for item in sublist]
print("Result:", result3)

'''
Method 4: Using itertools.chain() function
'''
from itertools import chain
print("\nMethod 4: Using itertools.chain() function")
result4 = list(chain(list1, list2))
print("Result:", result4)

'''
Method 5: Using the '*' operator with unpacking
'''
print("\nMethod 5: Using the '*' operator with unpacking")
result5 = [*list1, *list2]
print("Result:", result5)

'''
Method 6: Using the append() method and a for loop
'''
print("\nMethod 6: Using the append() method and a for loop")
list4 = list1.copy()  # Create a copy to preserve original list1
for item in list2:
    list4.append(item)
print("Result:", list4)
