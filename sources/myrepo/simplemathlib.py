PI = 3.14159265358979323846

def add(a, b):
    """
    Adds two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts one number from another.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divides one number by another. Returns 'None' if division by zero.
    """
    if b == 0:
        return "Division by zero is not allowed."
    return a / b