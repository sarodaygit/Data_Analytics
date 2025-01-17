
# LAMDA Functions
"""
Lambda functions are small, anonymous functions that can have any number of arguments, but can only have one expression.
They are defined using the lambda keyword, which has the following syntax:
lambda arguments: expression
""" 

# Basic Arithmetic Operations
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
subtract = lambda x, y: x - y
print(subtract(5, 2))  # Output: 3
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12
divide = lambda x, y: x / y if y != 0 else "Division by zero not allowed"
print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))  # Output: Division by zero not allowed

# String Operations
uppercase = lambda s: s.upper()
print(uppercase("hello"))  # Output: HELLO

lowercase = lambda s: s.lower()
print(lowercase("WORLD"))  # Output: world
reverse_string = lambda s: s[::-1]
print(reverse_string("hello"))  # Output: olleh
string_length = lambda s: len(s)
print(string_length("hello"))  # Output: 5

# List Operations
# map(function, iterable, ...)
"""
The map() function applies a given function to each item of an iterable (list, tuple, etc.) and returns a list of the results.
function - The function to apply to each item of the iterable.
iterable - An iterable object like a list, tuple, etc.
"""
square_elements = lambda lst: list(map(lambda x: x**2, lst))
print(square_elements([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]

"""
filter(function, iterable)  
function: A function that returns True or False for each element in the iterable.
iterable: The iterable to filter (e.g., list, tuple, etc.).
"""
filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
print(filter_even([1, 2, 3, 4, 5]))  # Output: [2, 4]


# Conditional Lambda
is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0

# Sorting with Lambda
sort_by_length = lambda lst: sorted(lst, key=lambda x: len(x))
sort_by_last_char = lambda lst: sorted(lst, key=lambda x: x[-1])

# Functional Programming (Map, Filter, Reduce)
double = lambda lst: list(map(lambda x: x * 2, lst))
filter_odd = lambda lst: list(filter(lambda x: x % 2 != 0, lst))

#