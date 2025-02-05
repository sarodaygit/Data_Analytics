import concurrent.futures
import multiprocessing
import time
import os

def worker(queue):
    """Worker function that takes an item from the queue and processes it."""
    num = queue.get()  # Get a number from the queue
    pid = os.getpid()  # Get the current process ID
    print(f"Process {pid} - Working on {num}")
    time.sleep(2)  # Simulate a time-consuming task
    print(f"Process {pid} - Finished {num}")
    return f"Process {pid} completed {num * 2}"

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        queue = manager.Queue()

        # Add 5 numbers to the queue
        for i in range(5):
            queue.put(i + 1)

        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
            # Submit worker tasks to the pool
            futures = [executor.submit(worker, queue) for _ in range(5)]
            
            # Retrieve and print results as they complete
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(f"Main Process: Got result → {result}")

    print("All tasks completed.")
