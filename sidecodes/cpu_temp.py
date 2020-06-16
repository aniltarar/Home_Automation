#cpu_temp.py

from gpiozero import CPUTemperature
from time import sleep
import os

def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
while True:
    try:
        cpu = CPUTemperature()
        cpu_temp = print(cpu.temperature)
        sleep(1)
        RAM_stats = getRAMinfo()
        RAM_used = round(int(RAM_stats[1]) / 1000,1)
        print(RAM_used)
        sleep(1)
    except KeyboardInterrupt:
        break