# Comparison Examples in Python

# Equality (==)
a = 10
b = 20
print("Equality (==):")
print(a == b)  # False
print(a == 10)  # True

# Inequality (!=)
print("\nInequality (!=):")
print(a != b)  # True
print(a != 10)  # False

# Greater than (>)
print("\nGreater than (>):")
print(a > b)  # False
print(b > a)  # True

# Less than (<)
print("\nLess than (<):")
print(a < b)  # True
print(b < a)  # False

# Greater than or equal to (>=)
print("\nGreater than or equal to (>=):")
print(a >= b)  # False
print(a >= 10)  # True

# Less than or equal to (<=)
print("\nLess than or equal to (<=):")
print(a <= b)  # True
print(b <= a)  # False

# Comparison of Strings
str1 = "apple"
str2 = "banana"
print("\nComparison of Strings:")
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 > str2)   # False
print(str1 < str2)   # True

# Comparison of Lists
list1 = [1, 2, 3]
list2 = [1, 2, 4]
print("\nComparison of Lists:")
print(list1 == list2)  # False
print(list1 != list2)  # True
print(list1 < list2)   # True
print(list1 > list2)   # False

# Chained Comparisons
x = 5
print("\nChained Comparisons:")
print(1 < x < 10)  # True
print(10 < x < 20)  # False
print(1 == x < 10)  # False

# Using Comparisons in Conditional Statements
x = 15
print("\nUsing Comparisons in Conditional Statements:")
if x > 10:
    print("x is greater than 10")

if x <= 15:
    print("x is less than or equal to 15")

if x == 15:
    print("x is equal to 15")

if x != 20:
    print("x is not equal to 20")
