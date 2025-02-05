import os

# Step 1: Define a Windows path
# Using a raw string to avoid issues with backslashes
# file_path = r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\myrepo\sampledirectory"
# file_path = "C:\\Users\\ashwini\\OneDrive\\Documents\\training\\Data_Analytics\\sources\\myrepo\\sampledirectory"
root_path = "C:\\Users\\ashwini\\OneDrive\\Documents\\training\\Data_Analytics\\sources\\myrepo\\"
# root_path = r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\myrepo"
directory_path = root_path + "sampledirectory"
# directory_path = os.path.join(root_path, "sampledirectory")
file_path = directory_path + "example_file.txt"
file_path = os.path.join(directory_path, "example_file.txt")
binary_file_path = os.path.join(directory_path, "example_binary_file.bin")


# Step 1: Create a directory if it doesn't exist
if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"Directory created: {directory_path}")
else:
    print(f"Directory already exists: {directory_path}")

# Step 2: Demonstrating file modes

# 2.1 Read Mode ("r") - Will fail if the file doesn't exist
print("\nReading file in 'r' mode:")
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print(file.read())
else:
    print(f"File not found: {file_path} (expected for 'r' mode demo)")

# 2.2 Write Mode ("w") - Creates or overwrites the file
print("\nWriting to the file in 'w' mode (overwriting existing content):")
with open(file_path, "w") as file:
    file.write("This is the first line.\n")
    file.write("This file was created in 'w' mode.\n")
print(f"File written at: {file_path}")

# 2.3 Append Mode ("a") - Appends to the file
print("\nAppending to the file in 'a' mode:")
with open(file_path, "a") as file:
    file.write("This content was added using 'a' mode.\n")
print(f"Content appended to file at: {file_path}")

# 2.4 Read Mode ("r") again to verify
print("\nReading the file content after 'a' mode:")
with open(file_path, "r") as file:
    print(file.read())

# 2.5 Exclusive Creation Mode ("x") - Creates a file if it doesn't exist
print("\nCreating a file in 'x' mode:")
if not os.path.exists(os.path.join(directory_path, "exclusive_file.txt")):
    with open(os.path.join(directory_path, "exclusive_file.txt"), "x") as file:
        file.write("This file was created using 'x' mode.\n")
    print("File created using 'x' mode.")
else:
    print("File already exists, so 'x' mode skipped.")

# 2.6 Binary Write Mode ("wb") - Writes binary data
print("\nWriting binary data to a file in 'wb' mode:")
with open(binary_file_path, "wb") as file:
    file.write(b"This is binary data.\n")
print(f"Binary file written at: {binary_file_path}")

# 2.7 Binary Read Mode ("rb") - Reads binary data
# print("\nReading binary data from the file in 'rb' mode:")
# with open(binary_file_path, "rb") as file:
#     print(file.read())

# 2.8 Read and Write Mode ("r+") - Reads and writes without overwriting
print("\nDemonstrating 'r+' mode (read and write):")
with open(file_path, "r+") as file:
    content = file.read()  # Read existing content
    print("Existing content and doing something with content and writing it back:\n", content)
    file.write("\nAdding this line with 'r+' mode.")

# 2.9 Write and Read Mode ("w+") - Overwrites and reads
print("\nDemonstrating 'w+' mode (write and read):")
with open(file_path, "w+") as file:
    file.write("Overwritten content with 'w+' mode.\n")
    file.seek(0)  # Move cursor to the beginning
    print("New content:\n", file.read())

# 2.10 Append and Read Mode ("a+") - Appends and reads
print("\nDemonstrating 'a+' mode (append and read):")
with open(file_path, "a+") as file:
    file.write("Appending with 'a+' mode.\n")
    file.seek(0)  # Move cursor to the beginning
    print("Content after appending:\n", file.read())

# Step 3: Clean up (Optional)
print("\nCleaning up...")
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File deleted: {file_path}")
if os.path.exists(binary_file_path):
    os.remove(binary_file_path)
    print(f"Binary file deleted: {binary_file_path}")
if os.path.exists(directory_path):
    os.rmdir(directory_path)
#     print(f"Directory deleted: {directory_path}")

