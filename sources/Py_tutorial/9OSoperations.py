import os
from pathlib import Path

# Step 1: Define a Windows path
# Using a raw string to avoid issues with backslashes
# file_path = r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\Py_tutorial\sampledirectory"
# file_path = "C:\\Users\\ashwini\\OneDrive\\Documents\\training\\Data_Analytics\\sources\\Py_tutorial\\sampledirectory"
file_path = "C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial/sampledirectory/example.txt"




# Step 2: Create and write to the file
# print("Creating and writing to the file...")
# with open(file_path, "w") as file:
#     file.write("Hello, this is a test file for Windows paths.\n")
#     file.write("File operations are now easy!")

# # Step 3: Read the content of the file
# print("\nReading the file content:")
# with open(file_path, "r") as file:
#     print(file.read())

# Step 4: Rename the file
renamed_file_path = "C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial/sampledirectory/renamed_example.txt"
# if os.path.exists(file_path):
#     os.rename(file_path, renamed_file_path)
#     print(f"\nFile renamed to: {renamed_file_path}")

# # Step 5: Create a new directory
directory_path = r"C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial/sampledirectory/test_directory"
# if not os.path.exists(directory_path):
#     os.mkdir(directory_path)
#     print(f"\nDirectory created: {directory_path}")

# Step 6: Move the renamed file into the new directory
new_file_path = os.path.join(directory_path, "renamed_example.txt")
if os.path.exists(renamed_file_path):
    os.replace(renamed_file_path, new_file_path)
    print(f"\nFile moved to: {new_file_path}")

# # Step 7: List files in the directory
# print("\nContents of the directory:")
# print(os.listdir(directory_path))

# # Step 8: Clean up: Delete the file and directory
# if os.path.exists(new_file_path):
#     os.remove(new_file_path)
#     print(f"\nFile deleted: {new_file_path}")

# if os.path.exists(directory_path):
#     os.rmdir(directory_path)
#     print(f"Directory deleted: {directory_path}")
