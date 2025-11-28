# ---------------------------------------------------------
# TYPE() FUNCTION AND TYPECASTING EXAMPLES
# ---------------------------------------------------------

print("\n--- 1. TYPE() FUNCTION ---")

x = 10
y = 10.5
z = "Hello"
a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}
d = {"name": "Sachin", "age": 21}

print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
print(type(z))   # <class 'str'>
print(type(a))   # <class 'list'>
print(type(b))   # <class 'tuple'>
print(type(c))   # <class 'set'>
print(type(d))   # <class 'dict'>


print("\n--- 2. TYPECASTING (CONVERSION BETWEEN TYPES) ---")

# ----- Converting to int -----
print("\nTo int:")
print(int(10.9))        # float → int (drops decimal)
print(int(True))        # bool → int (True = 1)
print(int(False))       # bool → int (False = 0)
print(int("25"))        # str → int (only if numeric)


# ----- Converting to float -----
print("\nTo float:")
print(float(5))         # int → float
print(float("3.14"))    # str → float


# ----- Converting to string -----
print("\nTo str:")
print(str(100))         # int → str
print(str(3.14))        # float → str
print(str([1, 2, 3]))   # list → str


# ----- Converting to list -----
print("\nTo list:")
print(list("Hello"))    # str → list of characters
print(list((1, 2, 3)))  # tuple → list


# ----- Converting to tuple -----
print("\nTo tuple:")
print(tuple([1, 2, 3]))     # list → tuple
print(tuple("ABC"))         # str → tuple


# ----- Converting to set -----
print("\nTo set:")
print(set([1, 2, 2, 3]))    # duplicates removed
print(set("hello"))         # unique letters only


# ----- Converting to bool -----
print("\nTo bool:")
print(bool(0))          # False
print(bool(10))         # True
print(bool(""))         # False
print(bool("Hello"))    # True
print(bool([]))         # False


print("\n--- 3. SPECIAL CASES / IMPORTANT NOTES ---")
# Typecasting rules that often confuse beginners

# 1. You cannot convert non-numeric strings to int
try:
    print(int("Sachin"))     # Error
except:
    print("Cannot convert 'Sachin' to int")

# 2. float → int removes decimal (no rounding)
print("int(9.99) =", int(9.99))   # Output: 9

# 3. bool → int → float chain
print(int(True), float(True))     # 1, 1.0
print(int(False), float(False))   # 0, 0.0

# 4. Empty structures are False in bool()
print(bool([]))      # False
print(bool({}))      # False
print(bool(""))      # False

# 5. Non-empty structures are True
print(bool([1]))     # True
print(bool("A"))     # True
