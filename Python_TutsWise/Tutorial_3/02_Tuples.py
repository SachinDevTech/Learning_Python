"""Tuples: A tuple in Python is an ordered collection of immutable elements, suitable for storing heterogeneous data."""

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
new_tuple = ("Helllooowww!",) #comma is a must while there is only one value in a tuple otherwise it will not be treated as tuple.
print(type(new_tuple))

# Accessing elements in a tuple
print("First element:", my_tuple[0])  # Output: 1
print("Last element:", my_tuple[-1])  # Output: 5

# Slicing a tuple
print("Sliced tuple:", my_tuple[1:3])  # Output: (2, 3)

# Unpacking a tuple
a, b, c, d, e = my_tuple
print("Unpacked elements:", a, b, c, d, e)  # Output: 1 2 3 4 5

# Tuple concatenation
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Finding the index of an element in a tuple
index = my_tuple.index(3)
print("Index of element 3:", index)  # Output: 2

# Counting occurrences of an element in a tuple
count = my_tuple.count(3)
print("Number of occurrences of 3:", count)  # Output: 1

# Length of a tuple
length = len(my_tuple)
print("Length of the tuple:", length)  # Output: 5

# Checking membership in a tuple
is_present = 5 in my_tuple
print("Is 5 present in the tuple?", is_present)  # Output: True

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Tuple packing
packed_tuple = 1, 2, 3
print("Packed tuple:", packed_tuple)  # Output: (1, 2, 3)

# Nested tuples
nested_tuple = (1, (2, 3), 4)
print("Nested tuple:", nested_tuple)  # Output: (1, (2, 3), 4)

# Immutable nature of tuples (Trying to modify a tuple will result in an error)
# Uncomment the line below to see the error
# my_tuple[0] = 0  # This will raise TypeError: 'tuple' object does not support item assignment
