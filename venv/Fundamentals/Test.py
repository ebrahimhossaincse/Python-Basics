'''
List
'''

list = [1,2,4,5,6,7,8,9]
print(list)
print('Length', len(list))

list.reverse()
print('Reverse', list)

list.sort()
print("Sort", list)

print('Specific Element', list[1])

print('Slice from index 0 to 3', list[0:3])

list.append(10)
print('Appending an element', list)

list.insert(1,11)
print('Insert', list)

list.extend([15,16,17])
print('Extending a List with Another List:', list)

list.remove(1)
print('Remove', list)

del list[0]
print('Delete', list)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print('Join', list1+list2+list3)

list1.extend(list2)
print('Extent', list1)

list4 = [1,2,4,5,6,7,8,9]

print("Method 1: Using a for loop")
for item in list4:
    print(item)

print("\nMethod 2: Using range() function")
for i in range(len(list4)):
    print(list4[i])

print("\nMethod 3: Using enumerate() function")
for index, value in enumerate(list4):
    print('Index', index, 'Value', value)

print("\nMethod 4: Using list comprehension")
[print(item) for item in list4]

print("\nMethod 5: Using while loop")
index = 0
while index < len(list4):
    print(list4[index])
    index += 1

