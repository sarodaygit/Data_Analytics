# Python File: Demonstrating Loops and Control Statements

# 1. For Loop: Iterating Over a List
# Demonstrates a simple for loop to iterate through a list of items
fruits = ['apple', 'banana', 'cherry']
print("Fruits in the list:")
for fruit in fruits:  # Loop through each fruit in the list
    print(fruit)  # Print the current fruit
print()  # Add a blank line for readability

# 2. For Loop with Range: Using range()
# Shows how to use the range() function with a for loop
print("Numbers from 0 to 4:")
for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)  # Print the current number
print()  # Add a blank line for readability

# 3. While Loop: Basic
# Example of a while loop, which runs until a condition becomes False
count = 0
print("Counting from 0 to 4 using while loop:")
while count < 5:  # Loop continues as long as count is less than 5
    print(count)  # Print the current count
    count += 1  # Increment count by 1 to avoid an infinite loop
print()  # Add a blank line for readability

# 4. Nested Loops: Nested For Loop
# Demonstrates a loop inside another loop (useful for 2D operations)
print("Nested For Loop:")
for i in range(3):  # Outer loop iterates 3 times (i = 0, 1, 2)
    for j in range(2):  # Inner loop iterates 2 times for each outer loop
        print(f"Outer: {i}, Inner: {j}")  # Print the current values of i and j
print()  # Add a blank line for readability

# 5. Loop Control Statements: Using break and continue
# Demonstrates how to control loops using break and continue statements

print("Combining break and continue:")
for num in range(10):
    if num == 7:  # Exit the loop when num is 7
        print("Breaking the loop at num =", num)
        break
    if num % 2 == 0:  # Skip even numbers
        continue  # Jump to the next iteration
    print(num)  # This will print odd numbers until the loop breaks
print("Loop ended.")
print()  # Add a blank line for readability

# Searching for a string starting with 'c' in a list
print("Searching for a string starting with 'c':")
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for fruit in fruits:
    if not fruit.startswith('c'):  # Skip strings that don't start with 'c'
        continue  # Jump to the next iteration
    print(f"First string starting with 'c': {fruit}")
    break  # Stop after finding the first match
print()  # Add a blank line for readability

# 6. Looping Through a Dictionary: Iterating Over a Dictionary
# Demonstrates iterating over keys and values in a dictionary
student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
print("Student Scores:")
for student, score in student_scores.items():  # items() returns key-value pairs
    print(f"{student}: {score}")  # Print the student's name and their score
print()  # Add a blank line for readability

# 7. Using while with else
print("Using while with else:")
count = 0
while count < 5:  # Loop while the condition is True
    print(f"Current count: {count}")  # Print the current count
    if count == 3:  # Break the loop when count is 3
        print("Breaking the loop when count is 3.")
        break  # Exit the loop prematurely
    count += 1  # Increment count
else:
    print("Loop ended naturally.")  # This won't execute because of the break
print("Exited the loop.")
print()  # Add a blank line for readability

# 8. Using pass in loops
# Example: for loop with pass
print("Using pass in a for loop:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    pass  # Placeholder to do nothing for now
print("Loop executed, but no action taken.")
