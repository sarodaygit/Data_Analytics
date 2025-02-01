class EvenNumbers:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration  # End iteration
        value = self.current
        self.current += 2  # Move to the next even number
        return value
    
if __name__ == "__main__":
    # Step 1: Simple for loop
    print("Step 1")
    print("Simple for loop example:")
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)

    # Step 2: How for loop works internally
    print("\nStep 2")
    print("\nHow for loop works internally:")
    iterator = iter(numbers)
    print(next(iterator))  # 1
    print(next(iterator))  # 2
    print(next(iterator))  # 3
    print(next(iterator))  # 4
    print(next(iterator))  # 5

    # Step 3: Custom Iterator for Even Numbers
    print("\nStep 3")
    print("\nCustom Iterator: Even Numbers")
    even_iterator = EvenNumbers(10)
    print(next(even_iterator))  # 0
    
    print("Fetching even numbers using a for loop:")
    for num in even_iterator:
        print(num)

    # Step 4: Large Dataset Justification
    print("\nStep 4")
    large_even_iterator = EvenNumbers(1000000)
    print("\nFetching first 5 even numbers from a large iterator:")
    for _ in range(5):  # Fetch only the first 5
        print(next(large_even_iterator))
    print("Did some work here")
    for _ in range(5):  # Fetch only the first 5
        print(next(large_even_iterator))