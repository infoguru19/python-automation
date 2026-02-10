import os
import time

LOG_DIR = "/path/to/logs"   # change this
LOG_EXTENSION = ".log"

ONE_MONTH_SECONDS = 30 * 24 * 60 * 60
current_time = time.time()

deleted_files = []

for root, dirs, files in os.walk(LOG_DIR):
    for file in files:
        if file.endswith(LOG_EXTENSION):
            file_path = os.path.join(root, file)
            file_mtime = os.path.getmtime(file_path)

            if current_time - file_mtime >= ONE_MONTH_SECONDS:
                #os.remove(file_path)
                print("Would delete:", file_path)
                deleted_files.append(file_path)

if deleted_files:
    print("Deleted log files older than one month:")
    for f in deleted_files:
        print(f)
else:
    print("No log files older than one month found.")
