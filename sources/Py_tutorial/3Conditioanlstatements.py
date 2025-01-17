# 1. Simple If Statement
print("Simple If Statement:")
# Check if a person is eligible to vote based on their age
age = 18
if age >= 18:  # Condition to check if age is 18 or older
    print("You are eligible to vote.")  # Executes if condition is True
else:
    print("You are not eligible to vote.")  # Executes if condition is False
print()  # Blank line for better readability

# 2. If-Elif-Else Statement
print("If-Elif-Else Statement:")
# Determine a grade based on the score
score = 85
if score >= 90:  # Check if the score is 90 or above
    print("Grade: A")
elif score >= 80:  # Check if the score is between 80 and 89
    print("Grade: B")
elif score >= 70:  # Check if the score is between 70 and 79
    print("Grade: C")
else:
    print("Grade: D")  # Executes if the score is below 70
print()

# 3. Nested If Statement
print("Nested If Statement:")
# Check if a number is positive and if it's even or odd
num = 15
if num > 0:  # Outer condition to check if the number is positive
    print("The number is positive.")
    if num % 2 == 0:  # Inner condition to check if the number is even
        print("It is also even.")
    else:
        print("It is odd.")  # Executes if the number is not even
else:
    print("The number is not positive.")  # Executes if the outer condition is False
print()

# 4. Using Logical Operators
print("Using Logical Operators:")
# Example to combine multiple conditions using logical operators
temperature = 30
is_raining = False
# Check if the temperature is greater than 25 AND it's not raining
if temperature > 25 and not is_raining:
    print("It's a nice day for a picnic.")
else:
    print("Better stay indoors.")  # Executes if any of the conditions are False
print()

# 5. Using the Ternary Operator
print("Using the Ternary Operator:")
# Find the maximum of two numbers using a ternary operator
x = 5
y = 10
max_value = x if x > y else y  # Ternary operator for concise decision-making
print(f"The maximum value is: {max_value}")  # Display the maximum value
print()

# 6. Input-Based Conditional OR Case Statements
print("Input-Based Conditional:")
# Prompt the user to enter a number and respond based on its value
user_input = input("Enter a number: ")  # Get input from the user
try:
    number = int(user_input)  # Convert input to an integer
    if number > 0:  # Check if the number is positive
        print("You entered a positive number.")
    elif number < 0:  # Check if the number is negative
        print("You entered a negative number.")
    else:
        print("You entered zero.")  # Executes if the number is exactly zero
except ValueError:  # Handle invalid input (e.g., non-numeric values)
    print("Invalid input! Please enter a valid number.")
