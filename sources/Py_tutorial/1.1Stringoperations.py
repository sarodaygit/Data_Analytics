# Python Practice: String Operations

# -----------------------------------------------------
# 1. Basic String Operations
# -----------------------------------------------------
print("Basic String Operations")
str1 = "Hello"
str2 = "World"

# Concatenation
print("Concatenation:", str1 + " " + str2)

# Repetition
print("Repetition:", str1 * 3)

# Indexing
print("Indexing:", str1[0])   # First character
print("Reverse Indexing:", str1[-1])  # Last character

# Slicing
print("Slicing (first 3 chars):", str1[:3])
print("Slicing (step of 2):", str1[::2])

# Length of a string
print("Length of str1:", len(str1))
print("-" * 40)

# -----------------------------------------------------
# 2. String Methods
# -----------------------------------------------------
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

# Checking Content
check_str = "Python123"
print("Starts with 'Py':", check_str.startswith("Py"))
print("Ends with '123':", check_str.endswith("123"))
print("Is digit:", check_str.isdigit())
print("Is alpha:", "Python".isalpha())
print("Is alphanumeric:", check_str.isalnum())
print("-" * 40)

# -----------------------------------------------------
# 3. Trimming and Padding
# -----------------------------------------------------
print("Trimming and Padding")
trim_str = "  Hello World  "
print("Strip:", trim_str.strip())
print("Left Strip:", trim_str.lstrip())
print("Right Strip:", trim_str.rstrip())
print("Center:", trim_str.center(20, "*"))
print("Left Justify:", trim_str.ljust(20, "-"))
print("Right Justify:", trim_str.rjust(20, "-"))
print("-" * 40)

# -----------------------------------------------------
# 4. Splitting and Joining
# -----------------------------------------------------
print("Splitting and Joining")
split_str = "Python,Java,C++"
languages = split_str.split(",")
print("Split by ',':", languages)

joined = " | ".join(languages)
print("Join with ' | ':", joined)
print("-" * 40)

# -----------------------------------------------------
# 5. String Formatting
# -----------------------------------------------------
print("String Formatting")
name = "Alice"
age = 25

# f-strings
print(f"My name is {name} and I am {age} years old.")

# format()
print("My name is {} and I am {} years old.".format(name, age))

# % formatting
print("My name is %s and I am %d years old." % (name, age))
print("-" * 40)

# -----------------------------------------------------
# 6. Practice Exercises
# -----------------------------------------------------
print("Practice Exercises")

# Exercise 1: Case Conversion
user_str = input("Enter a string: ")
print("Uppercase:", user_str.upper())
print("Lowercase:", user_str.lower())
print("Title Case:", user_str.title())

# Exercise 2: Search and Replace
sentence = input("Enter a sentence: ")
print("Replaced 'is' with 'was':", sentence.replace("is", "was"))

# Exercise 3: Validation
validation_str = input("Enter a string for validation: ")
print("Is digit:", validation_str.isdigit())
print("Is alpha:", validation_str.isalpha())
print("Is alphanumeric:", validation_str.isalnum())

# Exercise 4: Word Count
word_sentence = input("Enter a sentence: ")
words = word_sentence.split()
print("Word count:", len(words))

# Exercise 5: Palindrome Check
palindrome_str = input("Enter a string to check for palindrome: ")
if palindrome_str == palindrome_str[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
