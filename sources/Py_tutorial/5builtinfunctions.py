# Import the math library
import math

# === Built-in Functions Examples ===

# Absolute value
print("Absolute value of -10:", abs(-10))  # Output: 10

# Power function
print("2 raised to the power 3:", pow(2, 3))  # Output: 8

# Rounding numbers
print("Round 3.14159 to 2 decimal places:", round(3.14159, 2))  # Output: 3.14

# Type conversion
print("Convert '42' to integer:", int("42"))  # Output: 42
print("Convert '3.14' to float:", float("3.14"))  # Output: 3.14
print("Convert 123 to string:", str(123))  # Output: '123'

# Length, max, min, and sum
numbers = [1, 2, 3, 4, 5]
print("Length of the list:", len(numbers))  # Output: 5
print("Maximum in the list:", max(numbers))  # Output: 5
print("Minimum in the list:", min(numbers))  # Output: 1
print("Sum of the list:", sum(numbers))  # Output: 15

# Help and type
print("Type of 42:", type(42))  # Output: <class 'int'>
# Uncomment the line below to see documentation of the 'len' function
# help(len)

# === Math Library Functions Examples ===

# Square root
print("Square root of 25:", math.sqrt(25))  # Output: 5.0

# Factorial
print("Factorial of 5:", math.factorial(5))  # Output: 120

# Greatest common divisor
print("GCD of 12 and 18:", math.gcd(12, 18))  # Output: 6

# Ceiling and floor
print("Ceiling of 3.1:", math.ceil(3.1))  # Output: 4
print("Floor of 3.9:", math.floor(3.9))  # Output: 3

# Logarithms
print("Log base 10 of 100:", math.log(100, 10))  # Output: 2.0

# Trigonometric functions
print("Sine of pi/2:", math.sin(math.pi / 2))  # Output: 1.0
print("Cosine of 0:", math.cos(0))  # Output: 1.0
print("Tangent of pi/4:", math.tan(math.pi / 4))  # Output: 1.0

# Radians and degrees
print("Convert 180 degrees to radians:", math.radians(180))  # Output: 3.141592653589793
print("Convert pi radians to degrees:", math.degrees(math.pi))  # Output: 180.0

# Constants
print("Value of pi:", math.pi)  # Output: 3.141592653589793
print("Value of Euler's number e:", math.e)  # Output: 2.718281828459045
