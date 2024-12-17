# 🟢 MUTABLE OBJECTS

# 📝 Definition:
# Mutable objects can be changed after they are created.
# Examples: Lists, Dictionaries, Sets, and User-defined objects.

# Example of a Mutable Object (List)
my_list = [1, 2, 3]  # A list is a mutable object
print("Before modification:", my_list)  # Output: [1, 2, 3]

# Modify the list (change an element)
my_list[1] = 42  # Change the second element of the list
print("After modification:", my_list)  # Output: [1, 42, 3]

# 📝 Explanation:
# The list `my_list` was modified in place by changing the second element.
# Since lists are mutable, the original object is changed without creating a new one.

# ----------------------------------------------------------

# 🔴 IMMUTABLE OBJECTS

# 📝 Definition:
# Immutable objects cannot be changed after they are created.
# Examples: Strings, Tuples, Integers, Floats, Booleans, Frozensets.

# Example of an Immutable Object (String)
my_string = "Hello"  # A string is an immutable object
print("\nOriginal string:", my_string)  # Output: Hello

# Attempt to modify the string
my_string = my_string + " World"  # Concatenation creates a NEW string object
print("After modification:", my_string)  # Output: Hello World

# 📝 Explanation:
# When we add " World" to `my_string`, a new string object is created in memory.
# The original string "Hello" remains unchanged because strings are immutable.

# ----------------------------------------------------------

# 🔍 Key Differences Between Mutable and Immutable Objects
# ----------------------------------------------------------
# Feature          Mutable                          Immutable
# ----------------------------------------------------------
# Can be changed?   ✅ Yes (in-place modification)   ❌ No (new object is created)
# Data Types       List, Dict, Set, Custom Objects  Int, Float, String, Tuple, Bool, Frozenset
# Memory Impact    Changes in-place                New object created for changes
# Performance      Efficient (less memory)         Extra memory needed for changes

# ----------------------------------------------------------

# 🔥 Conceptual Understanding
# Mutable Types (like lists) allow us to update the existing object.
# This means we can add, remove, or change elements without creating a new object.
# 
# Immutable Types (like strings) don't allow changes to the original object.
# Instead, any modification results in the creation of a new object.

# ----------------------------------------------------------

# ✅ Demonstrating `id()` to show the memory difference between mutable and immutable objects

# For a mutable object (list)
print("\n🔍 Tracking memory for Mutable (List) object")
my_list = [1, 2, 3]
print("ID of original list:", id(my_list))  # Memory address of the original list
my_list.append(4)  # Modify the list (in-place change)
print("ID of list after append:", id(my_list))  # Same memory address as the original list
print("Updated list:", my_list)  # Output: [1, 2, 3, 4]

# 📝 Explanation:
# The memory address of the list remains the same after modification.
# This shows that the list is **mutable** as it was updated in place.

# ----------------------------------------------------------

# For an immutable object (string)
print("\n🔍 Tracking memory for Immutable (String) object")
my_string = "Hello"
print("ID of original string:", id(my_string))  # Memory address of the original string
my_string = my_string + " World"  # Concatenation creates a new string
print("ID of new string:", id(my_string))  # New memory address
print("Updated string:", my_string)  # Output: Hello World

# 📝 Explanation:
# The memory address of `my_string` changes after concatenation.
# This proves that the original string is **immutable**.

# 🚀 Quick Interview Questions
"""Q: Why are strings immutable in Python?
A: Strings are immutable for performance, security, and simplicity. When multiple variables point to the same string, memory is saved(Bachaana). If strings were mutable, changing one would affect all references to it."""

"""Q: What happens when you modify an integer?

A: Since integers are immutable, modifying them (like x += 1) creates a new object for x, and the old one is discarded if not referenced elsewhere because of automatic garbase collection."""

"""📚 Practice Questions
Identify if the following objects are mutable or immutable:"""

list = [1, 2, 3] #yes - mutable
tuple = (1, 2, 3) #no
num = 42 # no
set = {1, 2, 3} #yes - mutable


# HomeWork
# Q.1
"""What will be the output of the following code?
a = [1, 2, 3]
b = a
b[0] = 42
print(a)  # What will this print?"""

# Q.2
"""Write Python code to show how tuples are immutable using id() to track memory addresses."""