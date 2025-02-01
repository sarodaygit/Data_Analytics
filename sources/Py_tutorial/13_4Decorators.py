# With Decorator: Add logging using a reusable decorator
def logger(func):
    """
    A decorator that logs the function name and arguments before calling it.
    """
    def wrapper(*args, **kwargs):
        print(f"Logging: Calling {func.__name__} with arguments {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Without Decorator: Add logging manually to each function
def add(a, b):
    print(f"Logging: Calling add with arguments ({a}, {b})")
    return a + b

def multiply(a, b):
    print(f"Logging: Calling multiply with arguments ({a}, {b})")
    return a * b




# Apply the decorator to functions
@logger
def add_with_decorator(a, b):
    return a + b

@logger
def multiply_with_decorator(a, b):
    return a * b


if __name__ == "__main__":
    
    # Usage without decorator
    print("Without Decorator:")
    result_add = add(3, 5)
    print(f"Result of add: {result_add}")
    result_multiply = multiply(3, 5)
    print(f"Result of multiply: {result_multiply}")

    # Usage with decorator
    print("\nWith Decorator:")
    result_add_decorator = add_with_decorator(3, 5)
    print(f"Result of add_with_decorator: {result_add_decorator}")
    result_multiply_decorator = multiply_with_decorator(3, 5)
    print(f"Result of multiply_with_decorator: {result_multiply_decorator}")
