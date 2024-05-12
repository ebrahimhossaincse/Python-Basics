# Define a set
my_set = {"apple", "banana", "cherry", "orange"}

# Accessing set items directly
print("Set items:")
for item in my_set:
    print(item)
asdfasdf
# Checking if an item is in the set
print("\nChecking if 'banana' is in the set:")
if "banana" in my_set:
    print("'banana' is in the set")

# Accessing set items using indexing (not supported in sets)
try:
    print("\nAttempting to access set items using indexing:")
    print("First item:", my_set[0])  # This will raise an error
except TypeError as e:
    print("Error:", e)
    print("Sets do not support indexing")

# Converting a set to a list and then accessing items using indexing
set_to_list = list(my_set)
print("\nConverting set to list and accessing items using indexing:")
print("First item:", set_to_list[0])
