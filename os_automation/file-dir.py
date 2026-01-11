import os
new_dir = "/tmp/demo"
file_path = "demo.txt"

# Create Directory
os.makedirs( new_dir, exist_ok=True)
print(f"Directory Created: {new_dir}")

# Change Directory
os.chdir("/tmp/demo")
print("Current Directory",os.getcwd())

# Create File
with open(file_path, "w") as f:
    f.write("Hello From Python!\n")
print(f"File Created: {file_path}")

# list file
dir = "/tmp/demo"
items = os.listdir(dir)
print(items)                # Display as list
print(type(items))
for item in items:
    print(item)

print(f"{os.system("ls -lrt")}")
