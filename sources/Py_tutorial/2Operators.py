# Python Practice: Arithmetic, Comparison, and Logical Operators

# -----------------------------------------------------
# 1. Arithmetic Operators
# -----------------------------------------------------
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)           # 13
print("Subtraction:", a - b)        # 7
print("Multiplication:", a * b)     # 30
print("Division:", a / b)           # 3.3333...
print("Floor Division:", a // b)    # 3
print("Modulus:", a % b)            # 1
print("Exponentiation:", a ** b)    # 1000

print("-" * 40)

# -----------------------------------------------------
# 2. Comparison Operators
# -----------------------------------------------------
x = 5
y = 10

print("Comparison Operators")
print("Equal to:", x == y)           # False
print("Not equal to:", x != y)       # True
print("Greater than:", x > y)        # False
print("Less than:", x < y)           # True
print("Greater or equal:", x >= y)   # False
print("Less or equal:", x <= y)      # True

print("-" * 40)

# -----------------------------------------------------
# 3. Logical Operators
# -----------------------------------------------------
a = True
b = False

print("Logical Operators")
print("a and b:", a and b)           # False
print("a or b:", a or b)             # True
print("not a:", not a)               # False

# Combining comparison and logical operators
x = 15
print("Combining Operators")
print((x > 10) and (x < 20))         # True
print((x > 20) or (x == 15))         # True
print(not (x == 15))                 # False

print("-" * 40)

# -----------------------------------------------------
# 4. Practice Exercises
# -----------------------------------------------------
# Exercise 1: Arithmetic Operations with User Input
print("Exercise 1: Arithmetic Operations")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)

print("-" * 40)

# Exercise 2: Logical Comparison
print("Exercise 2: Logical Comparison")
number = int(input("Enter a number: "))
print("Is the number between 10 and 50?")
print((number > 10) and (number < 50))

print("-" * 40)

# Exercise 3: Evaluate Expression
print("Exercise 3: Evaluate Expression")
x = 5
y = 10
result = (x < y) and (x + y > 15)
print("Result of (x < y) and (x + y > 15):", result)


 #-----------------------------------------------------
# PEMDAS in Python
# -----------------------------------------------------
# PEMDAS stands for Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

# Example 1: Basic PEMDAS
# Expression: 3 + 6 * (5 ** 2) - 10 / 2
result1 = 3 + 6 * (5 ** 2) - 10 / 2

# Step-by-step breakdown:
# 1. Parentheses: (5 ** 2) = 25
# 2. Exponents: 6 * 25 = 150
# 3. Division: 10 / 2 = 5
# 4. Addition/Subtraction: 3 + 150 - 5 = 148
print("Example 1 - Result:", result1)  # Output: 148.0

# -----------------------------------------------------

# Example 2: Without Parentheses
# Expression: 3 + 6 * 5 ** 2 - 10 / 2
result2 = 3 + 6 * 5 ** 2 - 10 / 2

# Step-by-step breakdown:
# 1. Exponents: 5 ** 2 = 25
# 2. Multiplication: 6 * 25 = 150
# 3. Division: 10 / 2 = 5
# 4. Addition/Subtraction: 3 + 150 - 5 = 148
print("Example 2 - Result:", result2)  # Output: 148.0

# -----------------------------------------------------

# Example 3: Changing Precedence with Parentheses
# Expression: ((3 + 6) * 5) ** 2 / (10 - 2)
result3 = ((3 + 6) * 5) ** 2 / (10 - 2)

# Step-by-step breakdown:
# 1. Parentheses: (3 + 6) = 9, (10 - 2) = 8
# 2. Multiplication: 9 * 5 = 45
# 3. Exponents: 45 ** 2 = 2025
# 4. Division: 2025 / 8 = 253.125
print("Example 3 - Result:", result3)  # Output: 253.125

# -----------------------------------------------------

