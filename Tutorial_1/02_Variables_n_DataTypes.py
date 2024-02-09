#Variables: Named memory locations storing data for computer programs.
name = "Sachin Kumar"
age = 21
print(name, age)

# ------------------------------------------------

# DataTypes
'''
1. Integers
2. Boolean
3. String
4. None
5. Float
'''

#------------------------------------------------- 

#Keywords are the reserved word that can not be used as an identifier in our program as an variable. Ex. none, if, elif,etc.

# -----------------------------------------------

#Operators: Python operators facilitate various operations like arithmetic (addition +, subtraction -, multiplication *, division /, modulo % and power **), assignment (=), comparison (equality ==, inequality !=, less than <, greater than >), logical (and, or, not), bitwise (AND &, OR |, XOR ^), membership (in, not in), and identity (is, is not). They manipulate data and control program flow. For instance, arithmetic operators perform mathematical calculations, comparison operators compare values, and logical operators evaluate conditions. Each operator serves a distinct purpose in Python programming.


# Arithmetic operators
x = 10
y = 3
print("Arithmetic Operators:")
print("x + y =", x + y)  # Addition
print("x - y =", x - y)  # Subtraction
print("x * y =", x * y)  # Multiplication
print("x / y =", x / y)  # Division
print("x % y =", x % y)  # Modulus
print("x // y =", x // y)  # Floor Division
print("x ** y =", x ** y)  # Exponentiation

# Comparison operators
print("\nComparison Operators:")
print("x == y is", x == y)  # Equal to
print("x != y is", x != y)  # Not equal to
print("x < y is", x < y)  # Less than
print("x > y is", x > y)  # Greater than
print("x <= y is", x <= y)  # Less than or equal to
print("x >= y is", x >= y)  # Greater than or equal to

# Logical operators
a = True
b = False
print("\nLogical Operators:")
print("a and b is", a and b)  # Logical AND
print("a or b is", a or b)  # Logical OR
print("not a is", not a)  # Logical NOT

# Assignment operators
print("\nAssignment Operators:")
z = x + y  # Simple assignment
z += 2  # Add AND
print("z =", z)

# Membership operators
list_example = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print("2 in list_example is", 2 in list_example)  # Check if 2 exists in the list
print("6 not in list_example is", 6 not in list_example)  # Check if 6 does not exist in the list


# --------------------------------------------------

# Type Conversion - In Python, type conversion refers to the process of converting a value from one data type to another. Here are examples of various type conversions in Python:


import json  # Importing the json module for dictionary to string conversion

# Integer to Float
num_int = 5
num_float = float(num_int)
print(num_float)  # Output: 5.0

# Float to Integer
num_float = 3.14
num_int = int(num_float)
print(num_int)  # Output: 3

# String to Integer or Float
num_str = "10"
num_int = int(num_str)
num_float = float(num_str)
print(num_int, num_float)  # Output: 10 10.0

# Integer or Float to String
num_int = 10
num_float = 3.14
num_str_int = str(num_int)
num_str_float = str(num_float)
print(num_str_int, num_str_float)  # Output: "10" "3.14"

# String to List
str_example = "hello"
list_example = list(str_example)
print(list_example)  # Output: ['h', 'e', 'l', 'l', 'o']

# List to Tuple
list_example = [1, 2, 3]
tuple_example = tuple(list_example)
print(tuple_example)  # Output: (1, 2, 3)

# Tuple to List
tuple_example = (1, 2, 3)
list_example = list(tuple_example)
print(list_example)  # Output: [1, 2, 3]

# String to Dictionary (using eval() for simple cases)
str_dict = "{1: 'one', 2: 'two', 3: 'three'}"
dict_example = eval(str_dict)
print(dict_example)  # Output: {1: 'one', 2: 'two', 3: 'three'}

# Dictionary to String (using JSON)
dict_example = {1: 'one', 2: 'two', 3: 'three'}
str_dict = json.dumps(dict_example)
print(str_dict)  # Output: '{"1": "one", "2": "two", "3": "three"}'


# ------------------------------------------

# Type casting:

"""Typecasting refers to explicitly converting the data type of a value from one type to another. Here's the code with examples demonstrating typecasting along with comments:
"""

# -----------------------------------------------

#Input in python:

' In Python, you can take user input using the input() function. Here are examples of taking input from the user and using it in various contexts: '

# Simple Input and Output
name = input("Enter your name: ")
print("Hello,", name)

# Converting Input to Integer or Float
age = int(input("Enter your age: "))
print("You are", age, "years old")

height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters")

# Using Input in Calculations
radius = float(input("Enter the radius of a circle: "))
area = 3.14 * radius ** 2
print("The area of the circle is", area)

# Taking Multiple Inputs at Once
a, b = input("Enter two numbers separated by space: ").split()
print("First number:", a)
print("Second number:", b)

# Using List Comprehension to Process Input
numbers = [int(x) for x in input("Enter multiple numbers separated by space: ").split()]
print("Sum of numbers:", sum(numbers))

# Using Input in Conditions
password = input("Enter the password: ")
if password == "secret":
    print("Access granted!")
else:
    print("Access denied!")

# Using Input in Loops
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter student name: ")
    print("Hello,", name)
