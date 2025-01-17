import os

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
