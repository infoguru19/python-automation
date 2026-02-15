count = 0

with open("error.txt", "r") as f:

    for line_number, line in enumerate(f, start=1):
        if "error" in line:
            print(f"{line_number}: {line.strip()}")
            count +=1
    
print(f"Total number of EROOR= {count}")

