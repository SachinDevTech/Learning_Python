# ---------------------------------------------------------
# PYTHON OPERATORS – EXAMPLES WITH COMMENTS
# ---------------------------------------------------------

print("\n--- 1. ARITHMETIC OPERATORS ---")

a = 10
b = 3

print("a + b =", a + b)     # Addition → 13
print("a - b =", a - b)     # Subtraction → 7
print("a * b =", a * b)     # Multiplication → 30
print("a / b =", a / b)     # Division → 3.333...
print("a // b =", a // b)   # Floor Division → 3
print("a % b =", a % b)     # Modulus (remainder) → 1
print("a ** b =", a ** b)   # Exponent (power) → 10^3 = 1000


print("\n--- 2. COMPARISON OPERATORS (Relational) ---")

print("a == b:", a == b)    # Equal → False
print("a != b:", a != b)    # Not equal → True
print("a > b:", a > b)      # Greater than → True
print("a < b:", a < b)      # Less than → False
print("a >= b:", a >= b)    # Greater or equal → True
print("a <= b:", a <= b)    # Less or equal → False


print("\n--- 3. ASSIGNMENT OPERATORS ---")

x = 5
print("x =", x)

x += 2   # same as x = x + 2
print("x += 2 →", x)

x -= 1   # x = x - 1
print("x -= 1 →", x)

x *= 3   # x = x * 3
print("x *= 3 →", x)

x /= 2   # x = x / 2
print("x /= 2 →", x)

x //= 2  # x = x // 2
print("x //= 2 →", x)

x %= 3   # x = x % 3
print("x %= 3 →", x)

x **= 4  # x = x ** 4
print("x **= 4 →", x)


print("\n--- 4. LOGICAL OPERATORS ---")

p = True
q = False

print("p and q =", p and q)   # True only if both true
print("p or q =", p or q)     # True if any one is true
print("not p =", not p)       # Flips boolean value


print("\n--- 5. BITWISE OPERATORS ---")
# Operates on binary values

x = 5   # binary: 0101
y = 3   # binary: 0011

print("x & y =", x & y)       # AND → 1 (0001)
print("x | y =", x | y)       # OR  → 7 (0111)
print("x ^ y =", x ^ y)       # XOR → 6 (0110)
print("~x =", ~x)             # NOT → -6 (2's complement)
print("x << 1 =", x << 1)     # Left shift → 5 * 2 = 10
print("x >> 1 =", x >> 1)     # Right shift → 5 // 2 = 2


print("\n--- 6. MEMBERSHIP OPERATORS ---")

nums = [1, 2, 3, 4, 5]

print("3 in nums:", 3 in nums)        # True
print("10 not in nums:", 10 not in nums)  # True


print("\n--- 7. IDENTITY OPERATORS ---")

a = [1, 2, 3]
b = a         # b refers to same object
c = [1, 2, 3] # c is a different object with same values

print("a is b:", a is b)            # True (same memory location)
print("a is c:", a is c)            # False (different object)
print("a == c:", a == c)            # True (same values)


print("\n--- 8. TERNARY OPERATOR (Conditional Expression) ---")

age = 20
result = "Adult" if age >= 18 else "Minor"
print("Result:", result)


print("\n--- 9. OPERATOR PRECEDENCE EXAMPLE ---")

print("3 + 4 * 2 =", 3 + 4 * 2)        # Multiplication happens first → 11
print("(3 + 4) * 2 =", (3 + 4) * 2)    # Parentheses override → 14
