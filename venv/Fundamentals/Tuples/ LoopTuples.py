# Define a tuple
my_tuple = ("apple", "banana", "cherry", "orange")

# Loop through the tuple using a for loop
print("Looping through the tuple:")
for item in my_tuple:
    print(item)

# Accessing the index and item using enumerate
print("\nLooping through the tuple with index:")
for index, item in enumerate(my_tuple):
    print("Index:", index, "Item:", item)

# Loop through a tuple of tuples
tuple_of_tuples = ((1, "one"), (2, "two"), (3, "three"))
print("\nLooping through a tuple of tuples:")
for tpl in tuple_of_tuples:
    for item in tpl:
        print(item, end=" ")
    print()  # Move to the next line after printing each tuple

# Loop through a tuple and skip certain items
print("\nLooping through the tuple and skipping 'cherry':")
for item in my_tuple:
    if item == "cherry":
        continue  # Skip 'cherry'
    print(item)

# Loop through a tuple and break the loop when encountering a certain item
print("\nLooping through the tuple and breaking at 'cherry':")
for item in my_tuple:
    if item == "cherry":
        break  # Exit the loop when 'cherry' is encountered
    print(item)
