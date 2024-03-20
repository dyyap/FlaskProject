import psutil

print(
    "CPU Percentage:", psutil.cpu_percent(interval=0.1), "%"
)