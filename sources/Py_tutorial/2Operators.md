
# Python Practice: Arithmetic, Comparison, and Logical Operators

## Overview
This session introduces Python operators, focusing on arithmetic, comparison, logical operators, and PEMDAS (operator precedence). Students will engage in hands-on exercises to solidify their understanding.

---

## Topics Covered

### 1. Arithmetic Operators
- **Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Examples**:
  ```python
  a = 10
  b = 3
  print("Addition:", a + b)           # Output: 13
  print("Division:", a / b)           # Output: 3.3333...
  print("Exponentiation:", a ** b)    # Output: 1000
  ```

---

### 2. Comparison Operators
- **Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Examples**:
  ```python
  x = 5
  y = 10
  print("Greater than:", x > y)       # Output: False
  print("Less than or equal:", x <= y) # Output: True
  ```

---

### 3. Logical Operators
- **Operators**: `and`, `or`, `not`
- **Examples**:
  ```python
  a = True
  b = False
  print("a and b:", a and b)           # Output: False
  print("a or b:", a or b)             # Output: True
  print("not a:", not a)               # Output: False
  ```

- **Combining Operators**:
  ```python
  x = 15
  print((x > 10) and (x < 20))         # Output: True
  ```

---

### 4. Practice Exercises
1. **Arithmetic Operations with User Input**:
   - Prompt the user for two numbers and perform arithmetic operations.
   - Example:
     ```python
     num1 = int(input("Enter the first number: "))
     num2 = int(input("Enter the second number: "))
     print("Addition:", num1 + num2)
     ```

2. **Logical Comparison**:
   - Check if a number is within a specific range.
   - Example:
     ```python
     number = int(input("Enter a number: "))
     print((number > 10) and (number < 50))
     ```

3. **Evaluate Expression**:
   - Evaluate a logical expression combining comparison and logical operators.
   - Example:
     ```python
     x = 5
     y = 10
     result = (x < y) and (x + y > 15)
     print("Result:", result)
     ```

---

### 5. PEMDAS in Python
- **Order of Operations**:
  - Parentheses
  - Exponents
  - Multiplication/Division
  - Addition/Subtraction

- **Examples**:
  ```python
  # Example 1
  result1 = 3 + 6 * (5 ** 2) - 10 / 2
  print("Example 1 - Result:", result1)  # Output: 148.0

  # Example 3
  result3 = ((3 + 6) * 5) ** 2 / (10 - 2)
  print("Example 3 - Result:", result3)  # Output: 253.125
  ```

---

## Trainer Notes
1. **Introduce Concepts**:
   - Begin with basic operator explanations.
   - Highlight common pitfalls, like integer vs. float division.

2. **Interactive Sessions**:
   - Encourage students to try examples on their own systems.
   - Use live coding to demonstrate operator usage.

3. **Emphasize Practical Use**:
   - Relate exercises to real-world applications, such as validation (comparison) and calculations (arithmetic).

4. **Error Handling**:
   - Briefly discuss handling invalid inputs for user-driven exercises.

5. **Follow-Up**:
   - Assign additional practice problems.
   - Review key takeaways from PEMDAS examples.

---

## Learning Outcomes
By the end of the session, students should:
- Understand the usage and differences among arithmetic, comparison, and logical operators.
- Apply operators to solve problems effectively.
- Comprehend operator precedence and evaluate complex expressions.
