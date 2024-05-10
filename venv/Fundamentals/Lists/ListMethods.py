'''
List Methods Examples
'''

# Creating a list
my_list = [1, 2, 3, 4, 5]

# append() method
my_list.append(6)
print("append() Method:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# extend() method
my_list.extend([7, 8, 9])
print("extend() Method:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert() method
my_list.insert(2, 10)
print("insert() Method:", my_list)  # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# remove() method
my_list.remove(5)
print("remove() Method:", my_list)  # Output: [1, 2, 10, 3, 4, 6, 7, 8, 9]

# pop() method
popped_element = my_list.pop()
print("pop() Method - Popped Element:", popped_element)
print("pop() Method - Updated List:", my_list)  # Output: [1, 2, 10, 3, 4, 6, 7, 8]

# index() method
index_of_10 = my_list.index(10)
print("index() Method:", index_of_10)  # Output: 2

# count() method
count_of_10 = my_list.count(10)
print("count() Method:", count_of_10)  # Output: 1

# sort() method
my_list.sort()
print("sort() Method:", my_list)  # Output: [1, 2, 3, 4, 6, 7, 8, 10]

# reverse() method
my_list.reverse()
print("reverse() Method:", my_list)  # Output: [10, 8, 7, 6, 4, 3, 2, 1]

# copy() method
copied_list = my_list.copy()
print("copy() Method - Copied List:", copied_list)

# clear() method
my_list.clear()
print("clear() Method - Cleared List:", my_list)  # Output: []
