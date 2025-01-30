from pathlib import Path

# Define the base directory
BASE_DIR = Path("C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial")
NESTED_DIR = BASE_DIR / "sampledirectory/subdir1/subdir2"
FILE_NAME = NESTED_DIR / "exercise_file.txt"

def create_directories(nested_dir):
    """Create directories recursively."""
    try:
        nested_dir.mkdir(parents=True, exist_ok=True)
        print(f"Directories ensured: {nested_dir}")
    except Exception as e:
        print(f"Error creating directories: {e}")

def write_to_file(file_name, content):
    """Write initial content to the file."""
    try:
        print("\nCreating and writing to the file...")
        file_name.write_text(content)
        print(f"File '{file_name.name}' created and content written.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_file(file_name):
    """Read and return the file content."""
    try:
        if file_name.exists():
            print("\nReading the file content:")
            content = file_name.read_text()
            print(content)
            return content
        else:
            print(f"File '{file_name.name}' does not exist.")
    except Exception as e:
        print(f"Error reading file: {e}")

def append_to_file(file_name, additional_content):
    """Append content to the file."""
    try:
        print("\nAppending content to the file...")
        with file_name.open("a") as file:
            file.write(additional_content)
        print(f"Content appended to '{file_name.name}'.")
    except Exception as e:
        print(f"Error appending content: {e}")

def rename_file(file_name, new_name):
    """Rename the file."""
    try:
        new_file_path = file_name.parent / new_name
        file_name.rename(new_file_path)
        print(f"\nFile renamed to '{new_file_path.name}'.")
        return new_file_path  # Return new path for further use
    except Exception as e:
        print(f"Error renaming file: {e}")

def delete_file(file_name):
    """Delete the file."""
    try:
        if file_name.exists():
            print(f"\nDeleting the file '{file_name.name}'...")
            file_name.unlink()
            print("File deleted.")
        else:
            print(f"File '{file_name.name}' does not exist.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def delete_directories(base_dir, nested_dir):
    """Delete directories recursively from the bottom up."""
    try:
        print("\nDeleting directories...")
        current_dir = nested_dir
        while current_dir != base_dir:
            if any(current_dir.iterdir()):  # Check if directory is empty
                print(f"Skipping deletion (not empty): {current_dir}")
                break
            current_dir.rmdir()
            print(f"Deleted: {current_dir}")
            current_dir = current_dir.parent
    except Exception as e:
        print(f"Error deleting directories: {e}")

# Main Execution
if __name__ == "__main__":
    # Step 1: Create directories
    create_directories(NESTED_DIR)

    # Step 2: Write to the file
    write_to_file(FILE_NAME, "This is an exercise to practice modular file operations.\nPathlib is simple and powerful.\n")

    # Step 3: Read the file content
    read_file(FILE_NAME)

    # Step 4: Append additional content to the file
    append_to_file(FILE_NAME, "Adding more content to the file.\nPracticing Python is fun!\n")

    # Step 5: Read the updated file content
    read_file(FILE_NAME)

    # Step 6: Rename the file and update FILE_NAME
    FILE_NAME = rename_file(FILE_NAME, "updated_exercise_file.txt")  # Updating FILE_NAME

    # Step 7: Read the renamed file content
    read_file(FILE_NAME)  # Now correctly reads renamed file

    # Step 8: Delete the file
    delete_file(FILE_NAME)

    # Step 9: Delete the directories
    delete_directories(BASE_DIR, NESTED_DIR)
