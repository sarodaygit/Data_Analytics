class LogFileIterator:
    """Custom iterator to read a log file and dynamically filter log messages."""
    
    def __init__(self, file_path, filters=None):
        """
        Initializes the iterator.
        
        :param file_path: Path to the log file.
        :param filters: List of keywords to filter log lines (e.g., ["WARNING", "ERROR"]).
        """
        self.file_path = file_path
        self.file = open(file_path, "r", encoding="utf-8")  # Open the file
        self.filters = filters if filters else []  # If no filters, default to empty list

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        while True:
            line = self.file.readline()  # Read next line
            if not line:  # Stop when EOF is reached
                self.file.close()
                raise StopIteration
            
            # Check if any filter keyword is in the line
            if any(keyword in line for keyword in self.filters):
                return line.strip()  # Return the filtered line

if __name__ == "__main__":
    # Define log filters dynamically
    filters = ["WARNING", "ERROR", "CPU", "Disk space"]

    # Create an iterator with dynamic filters
    log_iterator = LogFileIterator("server_logs.txt", filters)

    print("\nFiltered Log Messages (Dynamic Filters Applied):")
    for log in log_iterator:
        print(log)
