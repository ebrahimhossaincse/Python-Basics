print('Example 1: Iterating over a list')
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print('\nExample 2: Iterating over a string')
for char in "Ebrahim":
    print(char)

print('\nExample 3: Iterating over a range of numbers')
for i in range(5):
    print(i)

print('\nExample 4: Iterating over a range of numbers with a specified start and end')
for i in range(1, 6):
    print(i)

print('\nExample 5: Iterating over a range of numbers with a specified step')
for i in range(0, 10, 2):
    print(i)

print('\nExample 6: Nested for loops')
for i in range(3):
    for j in range(2):
        print(i, j)

print('\nExample 7: Using else in a for loop')
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

print('\nExample 8: Using break in a for loop')
for i in range(5):
    if i == 3:
        break
    print(i)

print('\nExample 9: Using continue in a for loop')
for i in range(5):
    if i == 2:
        continue
    print(i)

print('\nExample 10: Iterating over a dictionary')
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)
