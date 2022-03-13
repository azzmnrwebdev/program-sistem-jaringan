# Nama  : Muhammad Azzam Nur Alwi Mansyur
# NIM   : 0110219060
# Kelas : Teknik Informatika-01 Pagi
# Tugas : Latihan Pertemuan04

import time
import sys
import subprocess
import multiprocessing

T1 = time.perf_counter()
hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '8.8.8.8', '8.8.4.4']
def do_something():
    status, result = subprocess.getstatusoutput("ping-c1" + ip_host)
    if (status == 0):
        print(f'Host {ip_host} is UP')
    else:
        print(f'Host {ip_host} is DOWN')

Processes = []
for x in range(len(hosts)):
    ip_host = hosts[x]
    P = multiprocessing.Process(target=do_something)
    P.start()
    Processes.append(P)
for process in Processes:
    process.join()
T2 = time.perf_counter()
print(f"Selesai dalam ... {round(T2-T1,2)}detik")