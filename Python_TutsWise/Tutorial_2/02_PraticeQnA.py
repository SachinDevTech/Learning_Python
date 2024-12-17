# Mathematical Questions and Solutions

# 1. Check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test
print("1. Check if a number is even or odd:")
print("Is 7 even or odd?", check_even_odd(7))
print("Is 10 even or odd?", check_even_odd(10))
print()

# 2. Check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test
print("2. Check if a number is prime:")
print("Is 13 prime?", is_prime(13))
print("Is 20 prime?", is_prime(20))
print()

# 3. Find the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Test
print("3. Find the factorial of a number:")
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print()

# 4. Check if a number is a multiple of another number
def is_multiple(number, multiple_of):
    if number % multiple_of == 0:
        return True
    else:
        return False

# Test
print("4. Check if a number is a multiple of another number:")
print("Is 15 a multiple of 3?", is_multiple(15, 3))
print("Is 20 a multiple of 7?", is_multiple(20, 7))
print()

# 5. Find the square of a number
def square(number):
    return number ** 2

# Test
print("5. Find the square of a number:")
print("Square of 8:", square(8))
print("Square of -4:", square(-4))
print()

# 6. Find the square root of a number
def square_root(number):
    return number ** 0.5

# Test
print("6. Find the square root of a number:")
print("Square root of 16:", square_root(16))
print("Square root of 2:", square_root(2))
print()

# 7. Find the sum of digits of a number
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Test
print("7. Find the sum of digits of a number:")
print("Sum of digits of 123:", sum_of_digits(123))
print("Sum of digits of 4567:", sum_of_digits(4567))
print()

# 8. Find the average of a list of numbers
def average(numbers):
    return sum(numbers) / len(numbers)

# Test
print("8. Find the average of a list of numbers:")
print("Average of [5, 10, 15, 20]:", average([5, 10, 15, 20]))
print("Average of [2, 4, 6, 8, 10]:", average([2, 4, 6, 8, 10]))
print()

# 9. Check if a number is a perfect square
def is_perfect_square(number):
    if number < 0:
        return False
    #if you wont type cast in int then will through an error.
    return int(number ** 0.5) ** 2 == number 

# Test
print("9. Check if a number is a perfect square:")
print("Is 25 a perfect square?", is_perfect_square(25))
print("Is 30 a perfect square?", is_perfect_square(30))
print()

# 10. Find the maximum and minimum of a list of numbers
def max_min(numbers):
    return max(numbers), min(numbers)

# Test
print("10. Find the maximum and minimum of a list of numbers:")
print("Max and min of [2, 8, 5, 10]:", max_min([2, 8, 5, 10]))
print("Max and min of [-3, 0, 9, -2]:", max_min([-3, 0, 9, -2]))
