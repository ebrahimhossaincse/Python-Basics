# Define a set
my_set = {"apple", "banana", "cherry", "orange"}

# Removing a specific item using remove() method
my_set.remove("banana")

# Print the set after removing an item
print("Set after removing 'banana':", my_set)

# Removing an item using discard() method
my_set.discard("cherry")

# Print the set after removing 'cherry'
print("Set after removing 'cherry':", my_set)

# Attempting to remove a non-existent item using remove() method (will raise an error)
try:
    my_set.remove("grape")
except KeyError as e:
    print("Error:", e)

# Removing an item using discard() method (even if it doesn't exist)
my_set.discard("grape")

# Removing and returning an arbitrary item from the set using pop() method
popped_item = my_set.pop()

# Print the popped item and the set after popping
print("Popped item:", popped_item)
print("Set after popping an item:", my_set)

# Removing all items from the set using clear() method
my_set.clear()

# Print the set after clearing all items
print("Set after clearing all items:", my_set)
