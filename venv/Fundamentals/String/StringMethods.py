'''
Converting case
'''
my_string = "Hello, World!"
print(my_string.upper())
print(my_string.lower())

'''
Splitting a string
'''
words = my_string.split(", ")
print(words)

'''
Checking if a string starts or ends with a specific substring
'''
print(my_string.startswith("Hello"))
print(my_string.endswith("World"))

'''
Finding the index of a substring
'''
index = my_string.find("World")
print(index)

'''
Replacing a substring
'''
new_string = my_string.replace("World", "Python")
print(new_string)

'''
capitalize() Method
'''
my_string = 'ebrahim'
capitalize = my_string.capitalize()
print (capitalize)

'''
casefold() Method
'''
my_string = 'EBRAHIM'
casefold = my_string.casefold()
print (casefold)

'''
count() Method
'''
my_string = "our Bridge Program helps you work towards your RN in less time."
count = my_string.count('you')
print (count)

'''
find() Method
'''
my_string = "our Bridge Program helps you work towards your RN in less time."
find = my_string.find('you')
print (find)

'''
upper() Method
'''
my_string = "our Bridge Program helps you work towards your RN in less time."
upper = my_string.upper()
print (upper)
