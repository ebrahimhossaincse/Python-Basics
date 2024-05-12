# Define a dictionary
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red",
    "engine": "V8"
}

# Removing an item from the dictionary using del keyword
del my_dict["color"]

# Print the dictionary after removing an item
print("Dictionary after removing 'color':", my_dict)

# Removing an item from the dictionary using pop() method
engine = my_dict.pop("engine")

# Print the dictionary and the popped item
print("Dictionary after popping 'engine':", my_dict)
print("Popped item:", engine)

# Removing an arbitrary item from the dictionary using popitem() method
removed_item = my_dict.popitem()

# Print the dictionary and the removed item
print("Dictionary after removing an arbitrary item:", my_dict)
print("Removed item:", removed_item)

# Clearing all items from the dictionary using clear() method
my_dict.clear()

# Print the dictionary after clearing all items
print("Dictionary after clearing all items:", my_dict)
