import os
import time

# Directory to search
LOG_DIR = "/Users/ranjanr/Downloads/"   # <-- change this
LOG_EXTENSION = ".yaml"

# One month in seconds (30 days)
ONE_MONTH_SECONDS = 30 * 24 * 60 * 60

current_time = time.time()

old_log_files = []

for root, dirs, files in os.walk(LOG_DIR):
    for file in files:
        if file.endswith(LOG_EXTENSION):
            file_path = os.path.join(root, file)
            file_mtime = os.path.getmtime(file_path)

            if current_time - file_mtime >= ONE_MONTH_SECONDS:
                old_log_files.append(file_path)


# Print results
if old_log_files:
    print("Log files older than one month:")
    for f in old_log_files:
        print(f)
else:
    print("No log files older than one month found.")
