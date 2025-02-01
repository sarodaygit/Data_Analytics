class EvenNumbersGenerator:
    """A class that generates even numbers lazily using a generator method."""
    
    def __init__(self, limit):
        self.limit = limit  # Store the limit

    def generate(self):
        """Generator method to yield even numbers up to the limit."""
        current = 0
        while current <= self.limit:
            yield current  # 'yield' remembers state
            current += 2

if __name__ == "__main__":
    # Step 1: Create an instance of the generator class
    even_gen_obj = EvenNumbersGenerator(1000000)

    # Step 2: Get the generator from the class method
    even_gen = even_gen_obj.generate()

    print("\nFetching first 5 even numbers from a large generator:")
    for _ in range(5):  # Fetch only the first 5 numbers
        print(next(even_gen))

    print("Did some work here...")

    print("\nFetching next 5 even numbers:")
    for _ in range(5):  # Fetch the next 5 numbers
        print(next(even_gen))
