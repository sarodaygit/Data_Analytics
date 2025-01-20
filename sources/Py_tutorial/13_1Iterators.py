import sys

# Without Iterator: Generate all squares and store them in a list
def generate_squares(n):
    """
    Generate a list of squares of numbers from 1 to n.
    """
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares

# Iterator-based solution
class SquaresIterator:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Main Program: Compare both approaches
if __name__ == "__main__":
    n = 5  # Example input size

    # Without Iterator
    print("\nSquares without iterator:")
    squares_list = generate_squares(n)
    for square in squares_list:
        print(square)

    # Memory usage without iterator
    print("\nMemory used without iterator:", sys.getsizeof(squares_list), "bytes")

    # With Iterator
    print("\nSquares using iterator:")
    squares_iterator = SquaresIterator(n)
    for square in squares_iterator:
        print(square)

    # Memory usage with iterator
    print("Memory used with iterator:", sys.getsizeof(squares_iterator), "bytes")

    # Comparing large input
    large_n = 1000000
    print("\nMemory Usage Comparison for Large Input:")
    
    # Without Iterator for large input
    large_squares_list = generate_squares(large_n)
    print(f"Memory used for list of size {large_n}:", sys.getsizeof(large_squares_list), "bytes")

    # With Iterator for large input
    large_squares_iterator = SquaresIterator(large_n)
    print(f"Memory used for iterator of size {large_n}:", sys.getsizeof(large_squares_iterator), "bytes")
