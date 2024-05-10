'''
List Examples
'''

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print("Accessing Elements:")
print("First element:", my_list[0])   # Output: 1
print("Last element:", my_list[-1])    # Output: 5

# Slicing
print("\nSlicing:")
print("Slice from index 1 to 3:", my_list[1:4])   # Output: [2, 3, 4]

# Appending an element
my_list.append(6)
print("\nAppending an Element:", my_list)   # Output: [1, 2, 3, 4, 5, 6]

# Modifying an element
my_list[0] = 0
print("\nModifying an Element:", my_list)   # Output: [0, 2, 3, 4, 5, 6]

# Removing an element
my_list.remove(3)
print("\nRemoving an Element:", my_list)   # Output: [0, 2, 4, 5, 6]

# Inserting an element at a specific index
my_list.insert(2, 3)
print("\nInserting an Element at Index 2:", my_list)   # Output: [0, 2, 3, 4, 5, 6]

# Extending a list with another list
my_list.extend([7, 8, 9])
print("\nExtending a List with Another List:", my_list)   # Output: [0, 2, 3, 4, 5, 6, 7, 8, 9]

# Deleting an element by index
del my_list[0]
print("\nDeleting an Element by Index:", my_list)   # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# Reversing the list
my_list.reverse()
print("\nReversing the List:", my_list)   # Output: [9, 8, 7, 6, 5, 4, 3, 2]

# Sorting the list
my_list.sort()
print("\nSorting the List:", my_list)   # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# Length of the list
print("\nLength of the List:", len(my_list))   # Output: 8
