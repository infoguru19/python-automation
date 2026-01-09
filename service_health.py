import subprocess

service = "nginx"

result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)

if result.stdout.strip() == "active":
    print("Service is running")
else:
    print("Service is DOWN")
