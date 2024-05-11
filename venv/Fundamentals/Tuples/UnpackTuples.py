'''
Define a tuple
'''
my_tuple = (1, 2, 3)

'''
Unpack the tuple into individual variables
'''
a, b, c = my_tuple

'''
Print the unpacked variables
'''
print("Unpacked variables:")
print("a =", a)
print("b =", b)
print("c =", c)

'''
Unpack a tuple with more elements than variables
'''
another_tuple = (10, 20, 30, 40, 50)
x, y, *rest = another_tuple

# Print the unpacked variables
print("\nUnpacked variables with *rest:")
print("x =", x)
print("y =", y)
print("*rest =", rest)

'''
Unpack a tuple nested within another tuple
'''
nested_tuple = ((1, 2), (3, 4), (5, 6))
(inner1, inner2, inner3) = nested_tuple

# Print the unpacked variables
print("\nUnpacked variables from nested tuple:")
print("inner1 =", inner1)
print("inner2 =", inner2)
print("inner3 =", inner3)
