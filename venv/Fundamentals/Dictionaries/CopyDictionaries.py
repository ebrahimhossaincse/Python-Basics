# Define a dictionary
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Shallow copy using the copy() method
copy_dict = my_dict.copy()

# Print the original and copied dictionaries
print("Original dictionary:", my_dict)
print("Copied dictionary:", copy_dict)

# Modifying the original dictionary
my_dict["year"] = 2022

# Print the dictionaries after modification
print("\nOriginal dictionary after modification:", my_dict)
print("Copied dictionary after modification:", copy_dict)

# Deep copy using the deepcopy() function from the copy module
import copy

deep_copy_dict = copy.deepcopy(my_dict)

# Print the original and deep copied dictionaries
print("\nOriginal dictionary:", my_dict)
print("Deep copied dictionary:", deep_copy_dict)

# Modifying the original dictionary
my_dict["brand"] = "Toyota"

# Print the dictionaries after modification
print("\nOriginal dictionary after modification:", my_dict)
print("Deep copied dictionary after modification:", deep_copy_dict)
