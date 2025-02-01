import functools

class Logger:
    """A simple class-based decorator that logs function calls."""
    
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)  # Preserve function metadata

    def __get__(self, instance, owner):
        """This ensures the decorator works correctly with instance methods."""
        return functools.partial(self.__call__, instance)

    def __call__(self, *args, **kwargs):
        print(f"🔹 Logging: Calling `{self.func.__name__}` with arguments {args} {kwargs}")
        return self.func(*args, **kwargs)  # Calls the function normally

class Calculator:
    """A simple calculator with basic operations."""

    @Logger
    def add(self, a, b):
        return a + b

    @Logger
    def multiply(self, a, b):
        return a * b

def main():
    calc = Calculator()
    
    print("🚀 **With Decorator (Logging Automatically):**\n")

    # Call methods
    print(calc.add(3, 5))
    print(calc.multiply(3, 5))

if __name__ == "__main__":
    main()
