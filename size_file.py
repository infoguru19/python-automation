import os

DIR = "/Users/ranjanr/Downloads"
SIZE_LIMIT = 2 * 1024 * 1024 * 1024 # 2GB

for root, dirs, files in os.walk(DIR):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)

        if file_size > SIZE_LIMIT:
            print(file_path)
            #os.remove(file_path)
          
