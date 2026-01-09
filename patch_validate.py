import subprocess

result = subprocess.run(
    ["uname", "-r"],
    capture_output=True,
    text=True
)

print(f"Current Kernel Version: {result.stdout}")
