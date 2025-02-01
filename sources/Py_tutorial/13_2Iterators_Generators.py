import sys

# Without Generator: Generate squares and store them in a list
def squares_without_generator(n):
    """
    Generate squares of numbers from 1 to n and store them in a list.
    Args:
        n (int): The upper limit of the range.
    Returns:
        list: A list of squares.
    """
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares

# With Generator: Generate squares lazily using yield
def squares_with_generator(n):
    """
    Generate squares of numbers from 1 to n lazily using a generator.
    Args:
        n (int): The upper limit of the range.
    Yields:
        int: The square of the current number.
    """
    for i in range(1, n + 1):
        yield i ** 2

# Infinite Sequence Example

def infinite_counter():
    count = 1
    while True:
        yield count
        count += 1


# Testing the functionality
if __name__ == "__main__":
    n = 10  # Input for demonstration

    # Without Generator
    print("\nWithout Generator:")
    squares_list = squares_without_generator(n)
    print("Squares:", squares_list)
    print("Memory used (list):", sys.getsizeof(squares_list), "bytes")

    # With Generator
    print("\nWith Generator:")
    squares_gen = squares_with_generator(n)
    print("Squares:", list(squares_gen))  # Converting generator to list for demonstration
    print("Memory used (generator):", sys.getsizeof(squares_gen), "bytes")

    # Demonstrating large input (memory comparison)
    large_n = 1000000
    print("\nMemory Usage Comparison for Large Input:")
    
    # Without Generator for large input
    large_squares_list = squares_without_generator(large_n)
    print(f"Memory used for list of size {large_n}:", sys.getsizeof(large_squares_list), "bytes")

    # With Generator for large input
    large_squares_gen = squares_with_generator(large_n)
    print(f"Memory used for generator of size {large_n}:", sys.getsizeof(large_squares_gen), "bytes")

    print("\nInfinite Sequence Example (Using Generator):")
    counter = infinite_counter()
    for _ in range(5):  # Printing first 5 values
        print(next(counter))
    print("Observe that counter continues indefinitely...")
    for _ in range(50):  # Printing next 50 values
        print(next(counter))
