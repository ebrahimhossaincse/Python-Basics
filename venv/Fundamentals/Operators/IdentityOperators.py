'''
Identity Operators Examples
'''

# is Operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("is Operator:")
print(x is z)  # Output: True, because x and z are the same object
print(x is y)  # Output: False, because x and y are different objects

# is not Operator
print("is not Operator:")
print(x is not z)  # Output: False, because x and z are the same object
print(x is not y)  # Output: True, because x and y are different objects