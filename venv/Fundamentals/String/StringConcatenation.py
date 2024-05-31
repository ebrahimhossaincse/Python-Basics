'''
Using the '+' operator
'''
greeting = "Hello"
name = "Ebrahim Hossain"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Ebrahim Hossain!


'''
Using the 'str.format()' method
'''
full_greeting = "{}, {}!".format(greeting, name)
print(full_greeting)  # Output: Hello, Ebrahim Hossain!


'''
Using f-strings (Python 3.6+)
'''
full_greeting = f"{greeting}, {name}!"
print(full_greeting)  # Output: Hello, Ebrahim Hossain!
