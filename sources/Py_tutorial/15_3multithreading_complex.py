
import concurrent.futures
import requests
import time
from pathlib import Path
import threading

STATUS_REPORT = Path("status_report.txt")
STATUS_REPORT.write_text("")
REPORT_LOCK = threading.Lock()

"""This  function shows how NOT to use a lock to prevent multiple threads from writing to a file at the same time."""
def get_status(url):
    current_text = STATUS_REPORT.read_text()
    print(f"Getting status of {url}")
    start_time = time.monotonic()
    response = requests.get(url)
    total_time = time.monotonic() - start_time
    print(f"Finished getting status of {url} in {total_time:.2f} seconds")
    STATUS_REPORT.write_text(f"{current_text}{url}: {response.status_code}\n")
    return url, response.status_code

"""
This makes the threads execute in sequence since we placed the lock in the wrong place.
The lock should be placed in the critical section of the code, where the file is being written to.
"""
# def get_status(url):
#     with REPORT_LOCK:
#         print(f"Getting status of {url}")
#         start_time = time.monotonic()
#         response = requests.get(url)
#         total_time = time.monotonic() - start_time
#         print(f"Finished getting status of {url} in {total_time:.2f} seconds")
#         current_text = STATUS_REPORT.read_text()
#         STATUS_REPORT.write_text(f"{current_text}{url}: {response.status_code}\n")
#     return url, response.status_code


"""this is the correct way to use a lock to prevent multiple threads from writing to a file at the same time."""
# def get_status(url):
#     print(f"Getting status of {url}")
#     start_time = time.monotonic()
#     response = requests.get(url)
#     total_time = time.monotonic() - start_time
#     print(f"Finished getting status of {url} in {total_time:.2f} seconds")
#     with REPORT_LOCK:
#         current_text = STATUS_REPORT.read_text()
#         STATUS_REPORT.write_text(f"{current_text}{url}: {response.status_code}\n")
#     return url, response.status_code


urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.github.com",
    "https://www.linkedin.com"
]

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for url in urls:
        future = executor.submit(get_status, url)
        futures.append(future)

    for future in concurrent.futures.as_completed(futures):
        try:
            url, code = future.result()
            print(f"Status code for {url} is {code}")
        except Exception as err:
            print(f"Task failed! {err}")