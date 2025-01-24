import os
from pathlib import Path

# Step 1: Define the absolute file path
file_path = "C:/Users/YourUsername/Documents/example_file.txt"

# Step 2: Create and write to the file
print("Creating and writing to the file...")
with open(file_path, "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file demonstrates file operations using an absolute path.\n")
print(f"File '{file_path}' created and initial content written.")

# Step 3: Read the content of the file
print("\nReading the file content:")
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# Step 4: Update the file (append content)
print("\nUpdating the file...")
with open(file_path, "a") as file:
    file.write("Adding a new line to the file.\n")
    file.write("File operations in Python with absolute paths are simple!")
print(f"Content appended to '{file_path}'.")

# Step 5: Read the updated content of the file
print("\nReading the updated file content:")
with open(file_path, "r") as file:
    updated_content = file.read()
    print(updated_content)

# Step 6: Rename the file
new_file_path = "C:/Users/YourUsername/Documents/renamed_file.txt"
print(f"\nRenaming the file to '{new_file_path}'...")
os.rename(file_path, new_file_path)
print(f"File renamed to '{new_file_path}'.")

# Step 7: Delete the file
print(f"\nDeleting the file '{new_file_path}'...")
os.remove(new_file_path)
print(f"File '{new_file_path}' deleted.")


# ###################### USING PATH LIB ############################


# # Using backslashes with raw string
# path_backslashes = Path(r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\Py_tutorial")

# # Using forward slashes
# path_forward_slashes = Path("C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial")

# # Both are equivalent
# print(path_backslashes)  # Outputs: C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\Py_tutorial
# print(path_forward_slashes)  # Outputs: C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\Py_tutorial


# Define the base directory
base_dir = Path(r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\Py_tutorial")
base_dir = Path("C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial")
sample_dir = base_dir / "sampledirectory"
file_name = sample_dir / "exercise_file.txt"

# Step 1: Create the directory if it doesn’t exist
try:
    if not sample_dir.exists():
        sample_dir.mkdir(parents=True)
        print(f"Directory '{sample_dir}' created.")
    else:
        print(f"Directory '{sample_dir}' already exists.")
except Exception as e:
    print(f"Error creating directory: {e}")

# Step 2: Create and write to the file
try:
    print("\nCreating and writing to the file...")
    file_name.write_text("This is an exercise to practice file operations.\nPathlib is simple and powerful.\n")
    print(f"File '{file_name.name}' created and content written.")
except Exception as e:
    print(f"Error writing to file: {e}")

# Step 3: Read and print the file content
try:
    print("\nReading the file content:")
    print(file_name.read_text())
except Exception as e:
    print(f"Error reading file: {e}")

# Step 4: Append additional content to the file (with context manager)
try:
    print("\nAppending content to the file...")
    with file_name.open("a") as file:  # Context manager ensures proper closure
        file.write("Adding more content to the file.\n")
        file.write("Practicing Python is fun!\n")
    print(f"Content appended to '{file_name.name}'.")
except Exception as e:
    print(f"Error appending content: {e}")

# Step 5: Read and print the updated file content
try:
    print("\nReading the updated file content:")
    print(file_name.read_text())
except Exception as e:
    print(f"Error reading updated content: {e}")

# Step 6: Rename the file
try:
    new_file_name = sample_dir / "updated_exercise_file.txt"
    file_name.rename(new_file_name)
    print(f"\nFile renamed to '{new_file_name.name}'.")
except Exception as e:
    print(f"Error renaming file: {e}")

# Step 7: Read and print the renamed file content
try:
    print("\nReading the renamed file content:")
    print(new_file_name.read_text())
except Exception as e:
    print(f"Error reading renamed file: {e}")

# Step 8: Delete the file (with context manager not required here)
try:
    print(f"\nDeleting the file '{new_file_name.name}'...")
    new_file_name.unlink()
    print("File deleted.")
except Exception as e:
    print(f"Error deleting file: {e}")

# Step 9: Delete the directory
try:
    print(f"\nDeleting the directory '{sample_dir.name}'...")
    sample_dir.rmdir()
    print("Directory deleted.")
except Exception as e:
    print(f"Error deleting directory: {e}")

