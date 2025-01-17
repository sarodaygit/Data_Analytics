# -----------------------------------------------------
# 1. Simple Data Types
# -----------------------------------------------------
# Integer
age = 25
print("Age:", age, "| Type:", type(age))

# Float
price = 19.99
print("Price:", price, "| Type:", type(price))

# String
name = "Alice"
print("Name:", name, "| Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "| Type:", type(is_student))

print("-" * 40)  # Separator

# -----------------------------------------------------
# 2. Type Conversion
# -----------------------------------------------------
# Converting between types
number = "123"
converted_number = int(number)
print("Original String:", number, "| Converted Integer:", converted_number, "| Type:", type(converted_number))

# Float to Integer
pi = 3.14159
integer_pi = int(pi)
print("Original Float:", pi, "| Converted Integer:", integer_pi)

# Integer to String
num = 42
string_num = str(num)
print("Original Integer:", num, "| Converted String:", string_num, "| Type:", type(string_num))

print("-" * 40)

# -----------------------------------------------------
# 3. Variables and Reassignment
# -----------------------------------------------------
# Declaring and reassigning variables
x = 10
print("Initial x:", x)

x = x + 5  # Reassigning
print("Updated x (x + 5):", x)

# Assigning multiple variables in one line
a, b, c = 1, 2, 3
print("Values of a, b, c:", a, b, c)

# Swapping variables
a, b = b, a
print("After Swapping: a =", a, "b =", b)

print("-" * 40)

# -----------------------------------------------------
# 4. Constants and Naming Conventions
# -----------------------------------------------------
# Constants (by convention, use ALL_CAPS)
PI = 3.14  # Not enforced, but considered constant
print("Value of PI (Constant):", PI)

# Snake_case naming convention
student_name = "John"
print("Student Name:", student_name)

print("-" * 40)

# -----------------------------------------------------
# 5. Dynamic Typing
# -----------------------------------------------------
# Changing variable types dynamically
value = 100  # Initially an integer
print("Value:", value, "| Type:", type(value))

value = "Python"  # Now a string
print("Value:", value, "| Type:", type(value))

value = 45.67  # Now a float
print("Value:", value, "| Type:", type(value))

print("-" * 40)

# -----------------------------------------------------
# 6. Input and Variables
# -----------------------------------------------------
# Accepting user input and determining its type
user_input = input("Enter something: ")
print("You entered:", user_input, "| Type:", type(user_input))

# Safely converting input to an integer
try:
    user_age = int(input("Enter your age (as a number): "))
    print("Your age is:", user_age, "| Type:", type(user_age))
except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("-" * 40)


#

#-----------------------------------------------------
# 7. Non Primitive Data Types
#-----------------------------------------------------
# List Variables
fruits = ["apple", "banana", "cherry"]
print("List Variables:")
print("Fruits:", fruits)
fruits.append("orange")  # Adding an element
print("Updated Fruits:", fruits)
print(f"Number of Fruits: {len(fruits)}\n")
mixed_list = [10, "Python", 3.14, True]
print("Mixed List:", mixed_list)
print(f"Second Element: {mixed_list[1]}\n")
duplicate_fruits = ["apple", "banana", "cherry", "apple"]
print("Duplicate Fruits:", duplicate_fruits)

# 5. Tuple Variables
coordinates = (10.0, 20.0)
print("Tuple Variables:")
print("Coordinates:", coordinates)
print(f"X: {coordinates[0]}, Y: {coordinates[1]}\n")
duplicate_coordinates = (10.0, 20.0, 10.0)
print("Duplicate Coordinates:", duplicate_coordinates)
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
print("List of Tuples:", list_of_tuples)

# 6. Dictionary Variables
student = {
    "name": "Bob",
    "age": 22,
    "courses": ["Math", "Science"]
}
print("Dictionary Variables:")
print("Student Info:", student)
print(f"Student Name: {student['name']}, Age: {student['age']}\n")

multiple_students = [  # Nested dictionary
    {"name": "Alice", "age": 22, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 23, "grade": "A"}]
print("Multiple Students:", multiple_students)
print(f"Second Student: {multiple_students[1]}\n")

dictionary_of_dicts = {  # Dictionary of dictionaries
    "student1": {"name": "Alice", "age": 22},
    "student2": {"name": "Bob", "age": 21},
}
print("Dictionary of Dicts:", dictionary_of_dicts)
print(f"Student 2 Info: {dictionary_of_dicts['student2']}\n")


# 7. Set Variables
unique_numbers = {1, 2, 3, 2, 1}
print("Set Variables:")
print("Unique Numbers:", unique_numbers)  # Duplicates are removed
unique_numbers.add(4)  # Adding an element
print("Updated Unique Numbers:", unique_numbers)
print(f"Number of Unique Numbers: {len(unique_numbers)}\n")


#-----------------------------------------------------
# 7. Exercises
# #-----------------------------------------------------
# Uncomment and solve the following exercises:

# Exercise 1: Declare a variable with your favorite number and print its type.
# favorite_number = ...
# print(...)

# Exercise 2: Take two inputs from the user, swap their values, and print the result.
# x = input("Enter first value: ")
# y = input("Enter second value: ")
# ... (swap x and y)
# print("Swapped values: x =", x, "y =", y)

# Exercise 3: Convert a float to an integer and print both values and their types.
# my_float = 10.75
# my_integer = ...
# print(...)






