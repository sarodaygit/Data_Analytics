import os
# from pathlib import Path

# Step 1: Define a Windows path
# Using a raw string to avoid issues with backslashes
# file_path = r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\Py_tutorial\sampledirectory"
# file_path = "C:\\Users\\ashwini\\OneDrive\\Documents\\training\\Data_Analytics\\sources\\Py_tutorial\\sampledirectory"
directory_path = r"C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial/sampledirectory"
file_path = "C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial/sampledirectory/example.txt"


if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"\nDirectory created: {directory_path}")


# # # Step 2: Create and write to the file
# print("Creating and writing to the file...")
# with open(file_path, "w") as file:
#     file.write("Hello, this is a test file for Windows paths.\n")
#     file.write("File operations are now easy!")

# #  Step 3: Read the content of the file
# print("\nReading the file content:")
# with open(file_path, "r") as file:
#     print(file.read())

# #  Step 4: Rename the file
# renamed_file_path = "C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial/sampledirectory/renamed_example.txt"
# if os.path.exists(file_path):
#     os.rename(file_path, renamed_file_path)
#     print(f"\nFile renamed to: {renamed_file_path}")


# # Step 5: Move the renamed file into a new subdirectory
# subfolder = "subfolder"
# new_subfolder_path = os.path.join(directory_path, subfolder)

# # Step 6: Create the subdirectory if it doesn't exist
# if not os.path.exists(new_subfolder_path):
#     os.mkdir(new_subfolder_path)
#     print(f"\nSubdirectory created: {new_subfolder_path}")
# new_file_path = os.path.join(new_subfolder_path, "renamed_example.txt")
# if os.path.exists(renamed_file_path):
#     os.rename(renamed_file_path, new_file_path)
#     print(f"\nFile moved to: {new_file_path}")

  

# Step 7: List contents of the subdirectory
# print("\nContents of the subdirectory:")
# print(os.listdir(new_subfolder_path))

# # Step 8: Clean up - Delete the file and directories (Optional)
# if os.path.exists(new_file_path):
#     os.remove(new_file_path)
#     print(f"\nFile deleted: {new_file_path}")

# if os.path.exists(new_subfolder_path):
#     os.rmdir(new_subfolder_path)
#     print(f"Subdirectory deleted: {new_subfolder_path}")

# if os.path.exists(directory_path):
#     os.rmdir(directory_path)
#     print(f"Main directory deleted: {directory_path}")
