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