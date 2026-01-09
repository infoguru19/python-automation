import shutil
import psutil

disk = shutil.disk_usage("/")
cpu = psutil.cpu_percent(interval=1)

print(f"Disk Free: {disk.free // (2**30)} GB")
print(f"CPU Usage: {cpu}%")

if disk.free < 5 * (2**30):
    print("WARNING: Low disk space")
