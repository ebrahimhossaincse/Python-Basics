'''
Using '%' operator (legacy)
'''
name = "Ebrahim"
age = 26
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

'''
Using 'str.format()' method
'''
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

'''
Using f-strings (Python 3.6+)
'''
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.
