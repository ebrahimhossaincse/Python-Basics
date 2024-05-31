import keyword

num = 1
print(num)

num2 = 10.2
print(num2)

name = 'Ebrahim'
print(name)

print(f'my name is {name}')

object = {'name: ': 'Ebrahim', 'age' : 22, 'city': 'Dhaka'}
print(object)

print(keyword.kwlist)

name = '20'
name2 = 20
print(name+str(name2))

list = [{1,2.3},{'name': 'ebrahim'}, 22]

x = {1,2,3,4,5,6}
y = {4,5,6,7,8,9}

print(x.union(y))
print(x.intersection(y))

NAME = 'EBRAHIM'
TIME = '9.00 AM'
message = "Good Morning, %s, It's %s" % (NAME, TIME)
print(message)

message = "Good Mornign, {}. It's {}".format(NAME, TIME)
print(message)

message = f"Good Morning, {NAME}. It's {TIME}"
print(message)

from string import Template
message = Template("Good Morning, $NAME. It's $TIME")
print(message.substitute(NAME=NAME, TIME=TIME))

# name = input()
# print(name)

input_string = input("Enter something, I will convert it to a list of words: ")
word_list = list(input_string)
print("List of words:", word_list)

