'''
Define a tuple
'''
my_tuple = (1, 2, 3, 4, 5)

'''
Attempting to update a tuple (which is not allowed)
'''
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be updated")

'''
However, you can create a new tuple with updated values
'''
updated_tuple = (10,) + my_tuple[1:]  # Concatenate a new value with the rest of the tuple
print("Updated tuple:", updated_tuple)

'''
Another example of updating a tuple
'''
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

'''
Reassigning a tuple variable to a new tuple
'''
my_tuple = updated_tuple
print("Reassigned tuple:", my_tuple)
