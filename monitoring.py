# Nama  : Muhammad Azzam Nur Alwi Mansyur
# NIM   : 0110219060
# Kelas : Teknik Informatika-01 Pagi
# Tugas : Latihan Pertemuan06

import os
from datetime import datetime as dt
import time as t
import concurrent.futures as cf

while True:
    timeStart = t.perf_counter()
    with open('D:\\Latihan\\jaringan\\peesje\\filenyaucup\\host.cfg') as file:
        readFile = file.read().splitlines()

    def checkping(ip):
        response = os.popen(f'ping {ip}').read()
        writeOutput = open(
            'D:\\Latihan\\jaringan\\peesje\\filenyaucup\\report-monitor.csv', 'a')
        if ('Received = 4') in response:
            writeOutput.write(f'{dt.now()};{ip};UP\n')
            return f'{dt.now()};{ip};UP'
        else:
            writeOutput.write(f'{dt.now()};{ip};DOWN\n')
            return f'{dt.now()};{ip};DOWN'

    with cf.ThreadPoolExecutor() as operator:
        print('Mulai monitor .....')
        result = operator.map(checkping, readFile)
        for f in result:
            print(f)
    timeEnd = t.perf_counter()
    t.sleep(10)

    print(f'Selesai dalam... {round(timeEnd-timeStart,2)} detik\n')