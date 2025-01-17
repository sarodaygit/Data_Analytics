
# Python Data Types: Trainer Notes

## Overview
This session covers both primary (primitive) and non-primitive data types in Python, along with interactive exercises for practice.

---

## 1. Primary (Primitive) Data Types

### Integer (`int`)
- Represents whole numbers.
- Supports arithmetic operations (e.g., addition, subtraction, multiplication, division).
- **Example**:
  ```python
  age = 25
  print(type(age))  # Output: <class 'int'>
  ```

### Float (`float`)
- Represents numbers with decimals.
- Useful for measurements or scientific calculations.
- **Example**:
  ```python
  pi = 3.14159
  print(type(pi))  # Output: <class 'float'>
  ```

### String (`str`)
- Represents textual data enclosed in quotes.
- Immutable and supports operations like slicing, concatenation.
- **Example**:
  ```python
  name = "Alice"
  print(type(name))  # Output: <class 'str'>
  ```

### Boolean (`bool`)
- Represents truth values (`True` or `False`).
- Commonly used in conditional logic.
- **Example**:
  ```python
  is_active = True
  print(type(is_active))  # Output: <class 'bool'>
  ```

### NoneType (`None`)
- Represents the absence of a value.
- **Example**:
  ```python
  value = None
  print(type(value))  # Output: <class 'NoneType'>
  ```

---

## 2. Non-Primitive Data Types

### List
- **Ordered**: Items have a defined order.
- **Mutable**: You can modify items (add, remove, update).
- **Allows Duplicates**.
- **Example**:
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.append("orange")
  print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
  ```

### Tuple
- **Ordered**: Items have a defined order.
- **Immutable**: Items cannot be modified after creation.
- **Allows Duplicates**.
- **Example**:
  ```python
  coordinates = (10.0, 20.0)
  print(coordinates[0])  # Output: 10.0
  ```

### Dictionary
- **Unordered**: Items have no specific order (insertion order preserved in Python 3.7+).
- **Key-Value Pairs**: Keys must be unique.
- **Example**:
  ```python
  student = {"name": "Bob", "age": 22}
  print(student["name"])  # Output: Bob
  ```

### Set
- **Unordered**: Items have no specific order.
- **Unique Elements**: Duplicates are automatically removed.
- **Example**:
  ```python
  unique_numbers = {1, 2, 3, 2}
  print(unique_numbers)  # Output: {1, 2, 3}
  ```

---

## 3. Interactive Exercises

### Primary Data Types
1. **Declare and Check Type**:
   ```python
   favorite_number = 7
   print("Favorite Number:", favorite_number, "| Type:", type(favorite_number))
   ```

2. **Arithmetic Operations**:
   ```python
   num1, num2 = 10, 20
   print("Sum:", num1 + num2)
   print("Difference:", num1 - num2)
   print("Product:", num1 * num2)
   print("Quotient:", num1 / num2)
   ```

### Non-Primitive Data Types
1. **Manipulating a List**:
   ```python
   colors = ["red", "green", "blue"]
   colors.append("yellow")
   print("Updated Colors:", colors)
   ```

2. **Swapping Tuple Values**:
   ```python
   a, b = 10, 20
   a, b = b, a
   print("Swapped: a =", a, "b =", b)
   ```

3. **Accessing a Dictionary**:
   ```python
   student = {"name": "Alice", "grade": "A"}
   print("Student Name:", student["name"])
   ```

4. **Performing Set Operations**:
   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   print("Union:", set1 | set2)
   print("Intersection:", set1 & set2)
   ```

---

## 4. Comparisons

| **Feature**        | **List**                | **Tuple**              | **Dictionary**           | **Set**                |
|---------------------|-------------------------|------------------------|--------------------------|------------------------|
| **Ordered**         | Yes                    | Yes                    | No                       | No                     |
| **Mutable**         | Yes                    | No                     | Yes                      | Yes                    |
| **Duplicates**      | Allowed                | Allowed                | Keys: No, Values: Yes    | No                     |
| **Access**          | By index (`list[0]`)   | By index (`tuple[0]`)  | By key (`dict['key']`)   | By iteration           |
| **Use Case**        | Dynamic collections    | Fixed collections      | Key-value relationships  | Unique collections     |

---

## 5. Trainer Tips
- Start with simple examples and build up to more complex data types.
- Use real-world analogies to explain concepts.
- Encourage students to experiment with examples during the session.
- Reinforce the importance of choosing the right data type for specific use cases.
