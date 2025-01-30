"""
Purpose of Exception Handling in Python:
- Prevents crashes by handling unexpected errors.
- Provides meaningful error messages to users.
- Ensures proper resource cleanup.
- Improves debugging and error tracking.
- Enables graceful recovery from failures.
- Maintains a smooth user experience.
"""

import requests

# Example 1: Preventing Program Crash
def prevent_crash():
    num = input("Enter a number to divide 10 by: ")
    try:
        num = float(num)
        print(10 / num)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    print("Program continues execution.")
    
    # Without exception handling (Uncomment to test crash)
    # num = float(input("Enter a number to divide 10 by: "))
    # print(10 / num)  # This would cause ZeroDivisionError if num is 0.

# Example 2: Providing Meaningful Error Messages
def file_handling():
    try:
        with open("missing.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Oops! The file you are trying to open does not exist.")
    
    # Without exception handling (Uncomment to test crash)
    # file = open("missing.txt", "r")  # This would cause FileNotFoundError

# Example 3: Ensuring Resource Cleanup
def file_cleanup():
    try:
        with open("example.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found.")
    finally:
        print("Cleaning up resources.")
    
    # Without exception handling (Uncomment to test crash)
    # file = open("example.txt", "r")
    # content = file.read()
    # print(content)  # If the file is missing, the program crashes.

# Example 4: Handling Multiple Errors
def multiple_exceptions():
    try:
        num = int(input("Enter a number (Test with 0, non-numeric, or a valid number): "))
        result = 10 / num
        print("Result:", result)
    except ValueError:
        print("Please enter a valid integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    
    # Without exception handling (Uncomment to test crash)
    # num = int(input("Enter a number: "))
    # result = 10 / num  # This would cause ZeroDivisionError if num is 0.
    # print("Result:", result)

# Example 5: Handling API Errors
def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Data fetched successfully:", response.json())
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Network error: Unable to connect to the server.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Without exception handling (Uncomment to test crash)
    # response = requests.get(api_url)
    # print("Data fetched successfully:", response.json())  # This would fail if the API is down.

# Testing Inputs
def test_cases():
    print("\n--- Running Test Cases ---")
    print("\nTest Case 1: Preventing Program Crash")
    prevent_crash()
    
    print("\nTest Case 2: Providing Meaningful Error Messages")
    file_handling()
    
    print("\nTest Case 3: Ensuring Resource Cleanup")
    file_cleanup()
    
    print("\nTest Case 4: Handling Multiple Errors")
    print("Enter '0' to test ZeroDivisionError, 'abc' to test ValueError, or '2' for valid input.")
    multiple_exceptions()
    
    print("\nTest Case 5: Handling API Errors")
    print("Testing with a valid API.")
    fetch_data("https://jsonplaceholder.typicode.com/posts/1")
    
    print("Testing with an invalid API.")
    fetch_data("https://invalid-api-url.com")

# Running Examples
if __name__ == "__main__":
    test_cases()
