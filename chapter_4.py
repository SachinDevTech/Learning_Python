# Learn input function of Python

# a = input("Are you a student: ").lower()
# isStudent = True if a == "yes" else False
# print(isStudent)



# ---------------------------------------------------------
# PYTHON INPUT() FUNCTION WITH EXAMPLES
# ---------------------------------------------------------

print("\n--- 1. Basic Input ---")

name = input("Enter your name: ")
print("Hello,", name)


print("\n--- 2. Input as Integer ---")

# input() always returns string → convert it to int
age = int(input("Enter your age: "))
print("Age after 5 years:", age + 5)


print("\n--- 3. Input as Float ---")

salary = float(input("Enter your salary: "))
print("With 10% bonus your salary will be:", salary * 1.10)


print("\n--- 4. Boolean Input (True/False) ---")

# Convert using lower() to avoid errors like: true/TRUE/TrUe
status = input("Are you a student? (yes/no): ").lower()
is_student = True if status == "yes" else False
print("Student status:", is_student)


print("\n--- 5. Taking Multiple Inputs in One Line ---")

# Example: Enter two numbers: 10 20
a, b = input("Enter two numbers: ").split()
print("You entered:", a, "and", b)

# Convert them to integers
a, b = map(int, input("Enter two integers: ").split())
print("Sum =", a + b)


print("\n--- 6. Taking List Input ---")

# Enter: 1 2 3 4 5
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("List:", numbers)
print("Max value:", max(numbers))


print("\n--- 7. Input as a List of Strings ---")

# Enter: apple mango banana
fruits = input("Enter fruits: ").split()
print("Fruits list:", fruits)


print("\n--- 8. Input a Character ---")

char = input("Enter a single character: ")[0]   # take first character only
print("You entered:", char)


print("\n--- 9. Using eval() for quick numeric input (dangerous but common in exams) ---")

x = eval(input("Enter any numeric value (int/float): "))
print("You entered:", x, "of type", type(x))


print("\n--- 10. Input with Default Value (using OR operator) ---")

# If user skips input → default value used
city = input("Enter your city (default Raipur): ") or "Raipur"
print("City:", city)
