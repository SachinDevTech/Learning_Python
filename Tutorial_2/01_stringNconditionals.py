#Strings : A datatype which is used to store sequence of characters. For Ex:
str1 = "Hii! Sachin."
str2 = 'Hii! Ashish.'
str3 = """Hii! Hrishabh."""

#escape sequence character like \t, \n
#adjusts just next content in new line
str4 = "Twinkle Twinkle Little Star, \nHow I wonder What you are." 
print(str4)
# ---------------------------------------------------------------
#add a tab space
str5 = "Twinkle Twinkle Little Star, \tHow I wonder What you are." 
print(str5)
# ---------------------------------------------------------------

#Operations on strings in python with examples

# String concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated string:", concatenated_str)

# String repetition
repeated_str = str1 * 3
print("Repeated string:", repeated_str)

# Accessing characters in a string
char_at_index = str1[1]
print("Character at index 1:", char_at_index)

# Slicing strings
substring = str2[1:4]
print("Substring:", substring)

# Length of a string
length_of_str = len(str1)
print("Length of string:", length_of_str)

# Checking substring existence
if "lo" in str1:
    print("Substring 'lo' found in", str1)
else:
    print("Substring 'lo' not found in", str1)

# String formatting
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print("Formatted string:", formatted_str)

# String methods
upper_case = str1.upper()
print("Uppercase:", upper_case)

lower_case = str2.lower()
print("Lowercase:", lower_case)

# Splitting strings
sentence = "This is a sample sentence."
words = sentence.split()
print("Words in the sentence:", words)

# Stripping whitespace
whitespace_str = "  Some text with whitespace   "
stripped_str = whitespace_str.strip()
print("Stripped string:", stripped_str)

# Replacing substrings
original_str = "I like apples"
replaced_str = original_str.replace("apples", "bananas")
print("Replaced string:", replaced_str)


# ---------------------------------------------------------------

'''String Functions: '''

# capitalize(): Converts the first character of a string to uppercase
string = "hello world"
capitalized_string = string.capitalize()
print("Capitalized string:", capitalized_string)

# casefold(): Converts a string into lowercase
string = "Hello World"
lowercase_string = string.casefold()
print("Lowercase string:", lowercase_string)

# count(): Returns the number of occurrences of a substring in the given string
string = "hello world, hello universe"
substring = "hello"
count = string.count(substring)
print("Number of occurrences of 'hello':", count)

# endswith(): Checks if a string ends with a specified suffix
string = "hello world"
suffix = "world"
ends_with = string.endswith(suffix)
print("String ends with 'world':", ends_with)

# find(): Returns the lowest index of the substring if found in the string, -1 otherwise
string = "hello world"
substring = "world"
index = string.find(substring)
print("Index of 'world':", index)

# isalnum(): Checks if all characters in a string are alphanumeric
string = "hello123"
is_alnum = string.isalnum()
print("Is alphanumeric:", is_alnum)

# isalpha(): Checks if all characters in a string are alphabetic
string = "hello"
is_alpha = string.isalpha()
print("Is alphabetic:", is_alpha)

# isdigit(): Checks if all characters in a string are digits
string = "123"
is_digit = string.isdigit()
print("Is digit:", is_digit)

# islower(): Checks if all characters in a string are lowercase
string = "hello"
is_lower = string.islower()
print("Is lowercase:", is_lower)

# isupper(): Checks if all characters in a string are uppercase
string = "HELLO"
is_upper = string.isupper()
print("Is uppercase:", is_upper)

# join(): Joins elements of an iterable (e.g., list) with a string separator
words = ["hello", "world"]
joined_string = "-".join(words)
print("Joined string:", joined_string)

# lstrip(): Removes leading whitespace characters from a string
string = "   hello world   "
stripped_string = string.lstrip()
print("Stripped string (leading):", stripped_string)

# rstrip(): Removes trailing whitespace characters from a string
string = "   hello world   "
stripped_string = string.rstrip()
print("Stripped string (trailing):", stripped_string)

# split(): Splits a string into a list of substrings based on a delimiter
string = "hello world"
words = string.split()
print("Split string:", words)

# startswith(): Checks if a string starts with a specified prefix
string = "hello world"
prefix = "hello"
starts_with = string.startswith(prefix)
print("String starts with 'hello':", starts_with)

# strip(): Removes leading and trailing whitespace characters from a string
string = "   hello world   "
stripped_string = string.strip()
print("Stripped string (leading and trailing):", stripped_string)

# swapcase(): Swaps the case of each character in a string
string = "Hello World"
swapped_string = string.swapcase()
print("Swapped case string:", swapped_string)

# title(): Converts the first character of each word to uppercase
string = "hello world"
title_string = string.title()
print("Titlecased string:", title_string)

# upper(): Converts all characters in a string to uppercase
string = "hello world"
uppercase_string = string.upper()
print("Uppercase string:", uppercase_string)

# zfill(): Pads a numeric string with zeros on the left to fill a specified width
string = "42"
padded_string = string.zfill(5)
print("Zfilled string:", padded_string)

# ---------------------------------------------------------------

'''Conditional Statements'''

# if statement
x = 10
if x > 0:
    print("x is positive")

# if-else statement
y = -5
if y >= 0:
    print("y is non-negative")
else:
    print("y is negative")

# if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z == 0:
    print("z is zero")
else:
    print("z is negative")

# Nested if statements
a = 15
if a > 0:
    print("a is positive")
    if a % 2 == 0:
        print("a is even")
    else:
        print("a is odd")

# Short-hand if statement
b = 20
print("b is positive") if b > 0 else print("b is non-positive")

# Short-hand if-else statement
c = -10
result = "positive" if c > 0 else "non-positive"
print("c is", result)

# Using logical operators in conditional statements
age = 25
if age >= 18 and age <= 65:
    print("You are of working age")
else:
    print("You are not of working age")

# Chained comparisons
num = 15
if 10 < num < 20:
    print("num is between 10 and 20")
else:
    print("num is not between 10 and 20")

# Using 'in' keyword to check membership
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Banana is in the list of fruits")
else:
    print("Banana is not in the list of fruits")