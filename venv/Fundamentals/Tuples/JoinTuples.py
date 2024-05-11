# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenate the tuples
concatenated_tuple = tuple1 + tuple2

# Print the concatenated tuple
print("Concatenated tuple:", concatenated_tuple)

# Alternatively, you can also use the `+=` operator to concatenate
tuple3 = (7, 8, 9)
tuple1 += tuple3
print("Concatenated tuple using += operator:", tuple1)

# Joining multiple tuples
tuple_of_tuples = ((1, 2), (3, 4), (5, 6))
joined_tuple = tuple()
for tpl in tuple_of_tuples:
    joined_tuple += tpl

# Print the joined tuple
print("Joined tuple:", joined_tuple)
