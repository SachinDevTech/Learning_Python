# A tuple is an ordered, immutable collection of elements.
# Once created, you cannot change or add/remove items in a tuple.

# ---------- Tuple Basics and Operations ----------

# Creating a tuple
person = ("Sachin", 22, "India")

# Accessing elements using index
print("Name:", person[0])        # Output: Sachin
print("Age:", person[1])         # Output: 22

# Slicing a tuple
print("Country:", person[2:])    # Output: ('India',)

# Length of a tuple
print("Length:", len(person))    # Output: 3

# Nested tuples
nested = ("A", (1, 2, 3))
print("Nested element:", nested[1][0])  # Output: 1

# Tuples are immutable (cannot change values)
# person[0] = "Rahul"  # ❌ This will raise a TypeError (Item assignment is not allowed!)

# Looping through tuple
print("\nLooping through tuple:")
for item in person:
    print(item)

# Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print("\nCount of 2:", nums.count(2))  # Output: 3
print("Index of 3:", nums.index(3))    # Output: 2

# Packing and unpacking
data = ("Sachin", 22, "India")
name, age, country = data
print(f"\nUnpacked: Name = {name}, Age = {age}, Country = {country}")

# Tuple as dictionary keys (tuples are hashable)
locations = {("Bangalore", "India"): "Karnataka"}
print("\nDictionary with tuple key:", locations[("Bangalore", "India")])

# Returning multiple values from function
def get_coordinates():
    return (12.97, 77.59)

lat, lon = get_coordinates()
print("\nCoordinates:", lat, lon)

# Performance: tuples use less memory and are faster than lists when data is fixed

# ---------- Practice Questions (Try yourself below) ----------

# 1. Create a tuple of 5 numbers. Print the max and min values.
# 2. Given a tuple of subjects = ("Math", "Physics", "Chemistry"), print them using a loop.
# 3. Swap values of two variables using tuple unpacking.
# 4. Write a function that takes a tuple of numbers and returns (sum, average).
# 5. Given a tuple with repeated values, write code to count how many times each value appears.

# Happy Coding!
