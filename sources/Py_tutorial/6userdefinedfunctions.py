# Define a basic function with no parameters
def greet():
    """
    Function to print a greeting message.
    """
    print("Hello, welcome to the demo of user-defined functions!")

# Define a function with parameters
def add_numbers(a, b):
    """
    Function to add two numbers.
    
    Parameters:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of a and b.
    """
    return a + b

# Define a function with default parameters
def greet_user(name="Guest"):
    """
    Function to greet a user with a default name if no name is provided.
    
    Parameters:
        name (str): The name of the user (default is "Guest").
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

# Define a function with only positional and keyword arguments
def positional_and_keyword(arg1, arg2, /, *, kwarg1, kwarg2):
    """
    Function demonstrating positional-only and keyword-only arguments.
    
    Parameters:
        arg1 (any): Positional-only argument.
        arg2 (any): Positional-only argument.
        kwarg1 (any): Keyword-only argument.
        kwarg2 (any): Keyword-only argument.
    
    Returns:
        str: A formatted string showing all arguments.
    """
    return f"Positional: {arg1}, {arg2}; Keyword: {kwarg1}, {kwarg2}"

# Define a function with variable-length positional arguments
def calculate_sum(*args):
    """
    Function to calculate the sum of any number of arguments.
    
    Parameters:
        *args (int): A variable-length list of numbers.
    
    Returns:
        int: The sum of all arguments.
    """
    return sum(args)

# Define a function with variable-length keyword arguments
def display_user(**kwargs):
    """
    Function to display user details using keyword arguments.
    
    Parameters:
        **kwargs: A dictionary of user details (key-value pairs).
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function with conditional logic
def is_even(num):
    """
    Function to check if a number is even.
    
    Parameters:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0

# Function to demonstrate local and global variables
x = 10  # Global variable

def modify_global():
    """
    Function to modify a global variable using the `global` keyword.
    """
    global x
    x += 5

# Main block to demonstrate the functions
if __name__ == "__main__":
    # 1. Basic function call
    greet()

    # 2. Function with parameters
    print("\nAdding numbers 5 and 7:")
    print(add_numbers(5, 7))  # Output: 12

    # 3. Function with default parameters
    print("\nGreeting with default parameter:")
    print(greet_user())  # Output: Hello, Guest!
    print("Greeting with custom parameter:")
    print(greet_user("Alice"))  # Output: Hello, Alice!

    # 4. Function with only positional and keyword arguments
    print("\nDemonstrating positional and keyword-only arguments:")
    print(positional_and_keyword(10, 20, kwarg1="Hello", kwarg2="World"))
    print(positional_and_keyword(10, 20, kwarg2="World", kwarg1="Hello"))
    # Output: Positional: 10, 20; Keyword: Hello, World

    # 5. Function with variable-length positional arguments
    print("\nCalculating sum of multiple numbers:")
    print(calculate_sum(1, 2, 3, 4, 5))  # Output: 15

    # 6. Function with variable-length keyword arguments
    print("\nDisplaying user details:")
    display_user(name="Bob", age=25, city="New York")

    # 7. Function with conditional logic
    print("\nChecking if numbers are even:")
    print(f"Is 4 even? {is_even(4)}")  # Output: True
    print(f"Is 7 even? {is_even(7)}")  # Output: False

    # 8. Function with local and global variables
    print("\nDemonstrating global variable modification:")
    print(f"Global variable before modification: {x}")  # Output: 10
    modify_global()
    print(f"Global variable after modification: {x}")  # Output: 15
