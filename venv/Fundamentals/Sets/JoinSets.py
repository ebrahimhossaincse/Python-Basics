# Define two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "kiwi", "grape"}

# Using the union() method to join sets (creates a new set with unique elements)
joined_set = set1.union(set2)

# Print the joined set
print("Joined set using union():", joined_set)

# Alternatively, you can use the pipe (|) operator for union
joined_set_alt = set1 | set2

# Print the joined set using the alternative method
print("Joined set using | operator:", joined_set_alt)
