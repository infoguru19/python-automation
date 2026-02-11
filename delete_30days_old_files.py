import os
import time

DIR = "/Users/ranjanr/python"
CURRENT_TIME = time.time()

ONE_MONTH = 30 * 24 * 60 * 60

for root, dirs, files in os.walk(DIR):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)

        try:
            if CURRENT_TIME - file_time > ONE_MONTH:
                print(file_path)
                #os.remove(file_path)
        except:
            pass
