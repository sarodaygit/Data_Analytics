# Comprehensions in Python
"""
[expression for item in iterable if condition]
- List Comprehension: Create a new list by applying an expression to each item in an iterable."""

# 1. List Comprehension
# Generate a list of squares
simplelist = [x for x in range(10)]
print("Simple List:", simplelist)
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)

# 2. Nested List Comprehension
# Generate a 2D grid
grid = [[x for x in range(3)] for y in range(3)]
print("Grid:", grid)

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flattened Matrix:", flat)

# 3. Dictionary Comprehension
# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(5)}
print("Squares Dictionary:", squares_dict)

# Filter a dictionary
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in original.items() if v % 2 == 0}
print("Filtered Dictionary:", filtered)

# 4. Sorting in Comprehensions
# Sort a list of numbers in descending order
sorted_list = [x for x in sorted([3, 1, 4, 1, 5, 9], reverse=True)]
print("Sorted List (Descending):", sorted_list)

# Dictionary sorted by keys
sorted_dict = {k: v for k, v in sorted({'c': 3, 'a': 1, 'b': 2}.items())}
print("Dictionary Sorted by Keys:", sorted_dict)

# Dictionary sorted by values
sorted_by_values = {k: v for k, v in sorted({'c': 3, 'a': 1, 'b': 2}.items(), key=lambda item: item[1])}
print("Dictionary Sorted by Values:", sorted_by_values)
