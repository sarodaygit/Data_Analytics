"""Multiprocessing is a great way to speed up CPU-bound tasks"""
import multiprocessing
import os  # Import os to get process ID

def square_sum(numbers):
    """Calculate the sum of squares of a list of numbers."""
    pid = os.getpid()  # Get the current process ID
    total = sum([num**2 for num in numbers])
    print(f"Process {pid} - Sum of squares from {numbers}: {total}")

if __name__ == "__main__":  # Prevents issues on Windows/macOS
    # Define the list of numbers to calculate the sum of squares for
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Divide the list into 2 chunks
    chunk1 = numbers[:5]
    chunk2 = numbers[5:]

    # Create processes
    process1 = multiprocessing.Process(target=square_sum, args=(chunk1,))
    process2 = multiprocessing.Process(target=square_sum, args=(chunk2,))

    print(f"Main Process ID: {os.getpid()}")  # Print the main process ID

    # Start processes
    process1.start()
    process2.start()

    # Wait for completion
    process1.join()
    process2.join()

    print("Multiprocessing completed!")
