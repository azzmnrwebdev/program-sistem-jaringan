# Nama  : Muhammad Azzam Nur Alwi Mansyur
# NIM   : 0110219060
# Kelas : Teknik Informatika-01 Pagi
# Tugas : Latihan Pertemuan05

import platform as p
import subprocess as sub
import time
import concurrent.futures
import threading

time1 = time.perf_counter()

def checkping(host):
    systemOs = '-n' if p.system().lower() == 'windows' else '-c'
    pinging = ['ping', systemOs, '1', host]
    status = ''
    time.sleep(1)

    if sub.call(pinging) == 0:
        status = 'UP'
    else:
        status = 'DOWN'

    output = '\nHost {} is {}'.format(host, status)

    print(output)

hosts = ['192.168.1.1','192.168.1.2','192.168.1.3','8.8.8.8','8.8.4.4']

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in hosts:
        result = [executor.submit(checkping,i)]
    for f in concurrent.futures.as_completed(result):
        print(f.result())

time2 = time.perf_counter()
print("")
print('Selesai dalam {} detik'.format(round(time2-time1,2)))