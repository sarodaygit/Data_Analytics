# """Threading adds new lanes for your program to execute"""
# import threading
# import time
# import random

# def print_names():
#     for name in ("John", "Kate", "Mike", "Alex", "Ann"):
#         print(name)
#         time.sleep(random.uniform(0.5, 1.5))

# def print_age(min_sleep, max_sleep):
#     for _ in range(5):
#         print(random.randint(20, 50))
#         time.sleep(random.uniform(min_sleep, max_sleep))

# t1 = threading.Thread(target=print_names)
# t2 = threading.Thread(target=print_age, args=(0.2, 1))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


"""Python threads aren't truly parallel, but are still useful for I/O bound tasks"""
import threading
import requests
from pathlib import Path

def download_file(url, filename):
    print(f"Downloading {url} to {filename}")
    response = requests.get(url)
    Path(filename).write_bytes(response.content)
    print(f"Finished downloading {filename}")

base_url = "https://raw.githubusercontent.com/JacobCallahan/Understanding/master/Python/file_io"
urls = [
    f"{base_url}/binary_file",
    f"{base_url}/files.py",
    f"{base_url}/names.txt",
    f"{base_url}/new_file.txt",
]

threads = []
for url in urls:
    filename = "downloads/" + url.split("/")[-1]
    t = threading.Thread(target=download_file, args=(url, filename))
    t.start()
    threads.append(t)

[t.join() for t in threads]