from pathlib import Path

# Define the base directory
base_dir = Path(r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\Py_tutorial")
sample_dir = base_dir / "sampledirectory"
file_name = sample_dir / "exercise_file.txt"

# Step 1: Create the directory if it doesn’t exist
if not sample_dir.exists():
    sample_dir.mkdir(parents=True)
    print(f"Directory '{sample_dir}' created.")
else:
    print(f"Directory '{sample_dir}' already exists.")

# Step 2: Create and write to the file
print("\nCreating and writing to the file...")
file_name.write_text("This is an exercise to practice file operations.\nPathlib is simple and powerful.\n")
print(f"File '{file_name.name}' created and content written.")

# Step 3: Read and print the file content
print("\nReading the file content:")
print(file_name.read_text())

# Step 4: Append additional content to the file
print("\nAppending content to the file...")
with file_name.open("a") as file:
    file.write("Adding more content to the file.\n")
    file.write("Practicing Python is fun!\n")
print(f"Content appended to '{file_name.name}'.")

# Step 5: Read and print the updated file content
print("\nReading the updated file content:")
print(file_name.read_text())

# Step 6: Rename the file
new_file_name = sample_dir / "updated_exercise_file.txt"
file_name.rename(new_file_name)
print(f"\nFile renamed to '{new_file_name.name}'.")

# Step 7: Read and print the renamed file content
print("\nReading the renamed file content:")
print(new_file_name.read_text())

# Step 8: Delete the file
print(f"\nDeleting the file '{new_file_name.name}'...")
new_file_name.unlink()
print("File deleted.")

# Step 9: Delete the directory
print(f"\nDeleting the directory '{sample_dir.name}'...")
sample_dir.rmdir()
print("Directory deleted.")
