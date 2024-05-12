# Define a set
my_set = {"apple", "banana", "cherry", "orange"}

# Loop through the set using a for loop
print("Looping through the set:")
for item in my_set:
    print(item)

# Looping through the set with index (not supported in sets)
try:
    print("\nAttempting to loop through the set with index:")
    for index, item in enumerate(my_set):  # This will raise an error
        print("Index:", index, "Item:", item)
except TypeError as e:
    print("Error:", e)
    print("Sets do not support indexing")

# Converting the set to a list and then looping through it with index
set_to_list = list(my_set)
print("\nConverting set to list and looping through it with index:")
for index, item in enumerate(set_to_list):
    print("Index:", index, "Item:", item)
