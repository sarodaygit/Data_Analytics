import os
# root_path =  r"C:\Users\ashwini\OneDrive\Documents\training\Data_Analytics\sources\myrepo"
# root_path = " C:\\Users\\ashwini\\OneDrive\\Documents\\training\\Data_Analytics\\sources\\myrepo\\"
root_path = "C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/myrepo/"
directory_path = os.path.join(root_path, "sampledirectory")
file_path = os.path.join(directory_path, "example_file.txt")

if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"Directory created: {directory_path}")

if os.path.exists(file_path):
    print(f"File already exists: {file_path}")
    with open(file_path, "r") as file:
        print(file.read())
else:
    print(f"this is expected . please create the file: {file_path}")
    
    
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("this the second line\n")
    print(f"File created: {file_path}")

with open(file_path, "a") as file:
    file.write("This content was added using 'a' mode.\n")
print(f"Content appended to file at: {file_path}")

if os.path.exists(file_path):
    print(f"File already exists: {file_path}")
    with open(file_path, "r") as file:
        print(file.read())
else:
    print(f"this is expected . please create the file: {file_path}")


if not os.path.exists(os.path.join(directory_path, "example_file2.txt")):
    print(f"File does not exist: {os.path.join(directory_path, 'example_file2.txt')}")
    with open(os.path.join(directory_path, "example_file2.txt"), "x") as file:
        file.write("This is a new file in the directory.")
    print(f"File created: {os.path.join(directory_path, 'example_file2.txt')}")
else:
    print(f"File already exists: {os.path.join(directory_path, 'example_file2.txt')}")