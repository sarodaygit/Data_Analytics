class FileSizeError(Exception):
    """Custom exception for file size errors."""
    def __init__(self, message):
        super().__init__(message)

# Example combining all aspects of exception handling
def exception_handling_demo(file_path, content):
    """
    Demonstrates all aspects of exception handling in Python:
    - `try`, `except`, `else`, and `finally`
    - Custom exceptions
    - Multiple exception handling

    :param file_path: Path to the file to read or write.
    :param content: Content to write into the file.
    """
    try:
        # Raise custom exception if content is too large
        if len(content) > 100:
            raise FileSizeError("Content size exceeds 100 characters.")

        # Writing to the file
        try:
            with open(file_path, "w") as file:
                file.write(content)
                print("Content written successfully.")
        except IOError as e:
            print(f"IOError occurred while writing: {e}")
        else:
            print("File written without any issues.")

        # Reading the file
        try:
            with open(file_path, "r") as file:
                data = file.read()
                print("File content:", data)
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")
        else:
            print("File read successfully.")

    except FileSizeError as e:
        print(f"Custom Exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("End of exception handling demo.")

# Example usage
if __name__ == "__main__":
    # Valid scenario
    print("--- Valid Scenario ---")
    exception_handling_demo("example.txt", "This is valid content.")

    # Triggering FileSizeError
    print("\n--- FileSizeError Scenario ---")
    letters = 'A' * 101
    exception_handling_demo("example.txt", letters)

    # Triggering FileNotFoundError
    print("\n--- FileNotFoundError Scenario ---")
    try:
        with open("non_existent_file.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found in separate block.")

    # Demonstrating PermissionError (optional, requires setting file permissions)
    print("\n--- PermissionError Scenario ---")
    try:
        with open("restricted_file.txt", "r") as file:
            print(file.read())
    except PermissionError:
        print("Error: Permission denied for restricted_file.txt.")

    print("\n--- Demo Completed ---")
