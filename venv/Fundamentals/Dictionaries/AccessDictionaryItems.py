# Define a dictionary
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Accessing dictionary items by key
brand = my_dict["brand"]
model = my_dict["model"]
year = my_dict["year"]

# Print the accessed items
print("Brand:", brand)
print("Model:", model)
print("Year:", year)

# Accessing dictionary items using get() method
model = my_dict.get("model")
color = my_dict.get("color", "No color specified")  # Providing a default value if the key doesn't exist

# Print the accessed items
print("\nModel:", model)
print("Color:", color)

# Accessing all keys and values in the dictionary using keys() and values() methods
print("\nAll keys in the dictionary:")
for key in my_dict.keys():
    print(key)

print("\nAll values in the dictionary:")
for value in my_dict.values():
    print(value)

# Accessing all key-value pairs in the dictionary using items() method
print("\nAll key-value pairs in the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)
