import os
import time

log_dir = "/var/log"
days = 7
now = time.time()

for file in os.listdir(log_dir):
    path = os.path.join(log_dir, file)
    if os.path.isfile(path):
        if now - os.path.getmtime(path) > days * 86400:
            os.remove(path)
            print(f"Deleted {file}")
