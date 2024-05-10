'''
Looping Through Lists Examples
'''

# List to loop through
my_list = [1, 2, 3, 4, 5]

# Method 1: Using a for loop
print("Method 1: Using a for loop")
for item in my_list:
    print(item)

# Method 2: Using range() function
print("\nMethod 2: Using range() function")
for i in range(len(my_list)):
    print(my_list[i])

# Method 3: Using enumerate() function
print("\nMethod 3: Using enumerate() function")
for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)

# Method 4: Using list comprehension
print("\nMethod 4: Using list comprehension")
[print(item) for item in my_list]

# Method 5: Using while loop
print("\nMethod 5: Using while loop")
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
