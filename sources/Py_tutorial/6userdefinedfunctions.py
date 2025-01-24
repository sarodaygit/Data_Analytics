# Define a basic function with no parameters

# Define a basic function with positional parameters
def greet(name, age = 18):
    print(f"Hello, {name}! You are {age} years old.")


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

def sub_numbers(a, b, /):
    """
    Function to add two numbers.
    
    Parameters:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of a and b.
    """
    return a - b

def multipy_numbers(*,a, b):
    """
    Function to add two numbers.
    
    Parameters:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of a and b.
    """
    return a * b


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

def flexible_function(a, b, *args, **kwargs):
    print(f"Positional arguments: a={a}, b={b}")
    print(f"Extra positional arguments (*args): {args}")
    print(f"Keyword arguments (**kwargs): {kwargs}")





# Main block to demonstrate the functions
if __name__ == "__main__":
     # Demonstrating positional arguments and default parameters
    greet("Alice", 25)
    greet(25, "Alice")  # Output: Hello, 25! You are Alice years old.
    # Calling the function using keyword arguments
    greet(name="Bob", age=20)  # Output: Hello, Alice! You are 25 years old.
    # Calling the function using keyword arguments (order doesn't matter)
    greet(age=20, name="Bob")  # Output: Hello, Bob! You are 20 years
    # Calling the function with one keyword argument and using the default value for the other
    greet(name="Bob")  # Output: Hello, Bob! You are 18 years old.


    # 2. Function with parameters
    print("\nAdding numbers 5 and 7:")
    print(add_numbers(5, 7))  # Output: 12

   # Demonstrating positional-only arguments
    print(sub_numbers(10, 3))  # Output 7
    print(sub_numbers(a=10, b= 3))  # Error since the function is defined with positional only arguments
    # Demonstrating keyword-only arguments
    print(multipy_numbers(a=10, b= 3))  # Output 30
    print(multipy_numbers(10, 3))  # Erro since the function is defined with keyword only arguments


    # 4. Function with only positional and keyword arguments
    print("\nDemonstrating positional and keyword-only arguments:")
    print(positional_and_keyword(10, 20, kwarg1="Hello", kwarg2="World"))
    print(positional_and_keyword(10, 20, kwarg2="World", kwarg1="Hello"))
    # Output: Positional: 10, 20; Keyword: Hello, World

    # # 5. Function with variable-length positional arguments
    # print("\nCalculating sum of multiple numbers:")
    print(calculate_sum(1, 2))  # Output: 3
    print(calculate_sum(1, 2, 3, 4, 5))  # Output: 15

    # # 6. Function with variable-length keyword arguments
    # print("\nDisplaying user details:")
    display_user(name="Bob", age=25, city="New York")
    display_user(username="Alice", role="Admin")

    # # 7. Function with conditional logic
    # print("\nChecking if numbers are even:")
    print(f"Is 4 even? {is_even(4)}")  # Output: True
    print(f"Is 7 even? {is_even(7)}")  # Output: False

    flexible_function(1, 2, 3, 4, 5, name="Alice", age=30)

    