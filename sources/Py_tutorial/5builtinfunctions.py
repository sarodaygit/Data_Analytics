# Import the math library
import math

def find_length(numbers):
    count = 0
    for num in numbers:
        count += 1  # Increment the counter for each element
    return count

def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.

    Parameters:
        numbers (list): A list of numbers.

    Returns:
        int: The sum of the numbers in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total




# Example Usage
numbers = [1, 2, 3, 4, 5]
length = find_length(numbers)
print("Length of the list Without Builtin function:", length)  # Output: Length of the list: 5
print("Length of the list:", len(numbers))  # Output: 5
sumofvalues = calculate_sum(numbers)
print("Sum of the list Without Builtin function:", sumofvalues)  # Output: Sum of the list: 15
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


print("String Methods")

# Case Conversion
case_str = "hello WORLD"
print("Lowercase:", case_str.lower())
print("Uppercase:", case_str.upper())
print("Capitalize:", case_str.capitalize())
print("Title Case:", case_str.title())
print("Swap Case:", case_str.swapcase())

# Search and Replace
search_str = "Hello World"
print("Find 'World':", search_str.find("World"))
print("Replace 'World' with 'Python':", search_str.replace("World", "Python"))
