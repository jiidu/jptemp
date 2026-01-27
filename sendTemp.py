import time
import serial
import psutil

try:
    import GPUtil
except ImportError:
    GPUtil = None

ser = serial.Serial('/dev/ttyACM0', 9600)

def get_cpu_package_temp():
    temps = psutil.sensors_temperatures()
    for entry in temps.get("coretemp", []):
        if entry.label == "Package id 0":
            return entry.current
    return None

def get_gpu_temp():
    temps = psutil.sensors_temperatures()

    # Intel iGPU
    for name in temps:
        if "gpu" in name.lower():
            return temps[name][0].current

    # NVIDIA / AMD dGPU
    if GPUtil:
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].temperature

    return None

while True:
    cpu = get_cpu_package_temp()
    gpu = get_gpu_temp()

    if cpu is not None and gpu is not None:
        msg = f"CPU:{cpu:.0f} GPU:{gpu:.0f}\n"
    elif cpu is not None:
        msg = f"CPU:{cpu:.0f} GPU:NA\n"
    else:
        msg = "CPU:NA GPU:NA\n"

    print("Sending:", msg.strip())
    ser.write(msg.encode("utf-8"))

    time.sleep(5) #Update interval

