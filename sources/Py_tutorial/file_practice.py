from pathlib import Path

BASE_DIR = Path("C:/Users/ashwini/OneDrive/Documents/training/Data_Analytics/sources/Py_tutorial")
NESTED_DIR = BASE_DIR / "sampledirectory/subdir1/subdir2"
FILE_NAME = NESTED_DIR / "exercise_file.txt"

def create_directories(directory):
    try:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Directory created at {directory}")
    except Exception as e:
        print(e)
        print("Failed to create directory")

def write_to_file(file_name, content):
    try:
        print("Creating and Writing to file...")
        with open(file_name, "w") as file:
            file.write(content)
        print(f"Content written to {file_name}")
    except Exception as e:
        print(e)
        print("Failed to write to file")
       
def read_file(file_name):
    try:
       if file_name.exists():
           print("Reading file...")
           content = file_name.read_text()
           print(content)
           return content
       else:
            print("File does not exist")
    except Exception as e:
        print(e)
        print("Failed to read file")

if __name__ == '__main__':
    create_directories(NESTED_DIR)
    write_to_file(FILE_NAME, "This is a sample content written to a file.")
    read_file(FILE_NAME)