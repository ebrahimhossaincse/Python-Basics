'''
Define a tuple
'''
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi")

'''
Accessing tuple items by index
'''
first_item = my_tuple[0]
second_item = my_tuple[1]
last_item = my_tuple[-1]

'''
Accessing tuple items using slicing
'''
sliced_items = my_tuple[1:4]  # from index 1 (included) to index 4 (excluded)

'''
Accessing tuple items using negative indexing
'''
second_last_item = my_tuple[-2]

'''
Printing the accessed items
'''
print("First item:", first_item)
print("Second item:", second_item)
print("Last item:", last_item)
print("Sliced items:", sliced_items)
print("Second last item:", second_last_item)
