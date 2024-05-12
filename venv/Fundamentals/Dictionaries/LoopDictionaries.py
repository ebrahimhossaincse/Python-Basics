'''
Define a dictionary
'''
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Loop through the dictionary using a for loop to access keys
print("Looping through the dictionary (keys):")
for key in my_dict:
    print(key)

# Loop through the dictionary using a for loop to access values
print("\nLooping through the dictionary (values):")
for value in my_dict.values():
    print(value)

# Loop through the dictionary using a for loop to access key-value pairs
print("\nLooping through the dictionary (key-value pairs):")
for key, value in my_dict.items():
    print(key, ":", value)

# Loop through the dictionary using items() method to access key-value pairs (alternative way)
print("\nLooping through the dictionary (key-value pairs using items()):")
for item in my_dict.items():
    print(item)

# Unpacking the key-value pairs while looping through the dictionary
print("\nLooping through the dictionary (unpacking key-value pairs):")
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
