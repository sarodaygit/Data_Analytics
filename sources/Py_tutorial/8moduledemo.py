# Import from my_package
import simplemodule
from mypackage import math_operations, string_operations
from mypackage.utilities import math_helpers, string_helpers

def main():
    print(simplemodule.add(5, 3))  # Output: 8

    # === Using math_operations module ===
    print("Basic Math Operations:")
    print("Add 5 + 3:", math_operations.add(5, 3))  # Output: 8
    print("Subtract 10 - 4:", math_operations.subtract(10, 4))  # Output: 6

    # === Using string_operations module ===
    print("\nString Operations:")
    print("Concatenate 'Hello' and 'World':", string_operations.concatenate("Hello", "World"))  # Output: HelloWorld
    print("Split 'Python is great':", string_operations.split_string("Python is great"))  # Output: ['Python', 'is', 'great']

    # === Using math_helpers submodule ===
    print("\nAdvanced Math Operations (Utilities):")
    print("Multiply 3 * 4:", math_helpers.multiply(3, 4))  # Output: 12
    print("Divide 10 / 2:", math_helpers.divide(10, 2))  # Output: 5.0

    # === Using string_helpers submodule ===
    print("\nAdvanced String Operations (Utilities):")
    print("Reverse 'Python':", string_helpers.reverse_string("Python"))  # Output: nohtyP
    print("Capitalize 'python is great':", string_helpers.capitalize_words("python is great"))  # Output: Python Is Great

if __name__ == "__main__":
    main()
