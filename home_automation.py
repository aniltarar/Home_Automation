# home_automation.py

from flask import Flask, render_template, request
from gpiozero import CPUTemperature
from time import sleep
import serial
import os
import paho.mqtt.client as mqtt
import requests

app = Flask(__name__)

url = 'http://api.openweathermap.org/data/2.5/weather?q=Sydney&appid=7565a75516d17107ec5400c12e57386e&units=metric'
ser = serial.Serial('/dev/ttyACM0', 9600)

@app.route("/")
def home():
    def getRAMinfo():
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                return(line.split()[1:4])
    
    
    res = requests.get(url)
    data = res.json()
    temp_city = data['main']['temp']
    
    RAM_stats = getRAMinfo()
    RAM_used = round(int(RAM_stats[1]) / 1000,1)
    cpu = CPUTemperature()
    cpu_temp1 = cpu.temperature
    cpu_temp = cpu_temp1
    
    ser = serial.Serial('/dev/ttyACM0', 9600)
    rawserial = ser.readline()
    cookedserial = rawserial.decode('utf-8').strip('\r\n')
    datasplit = cookedserial.split('-')
    temperature_dht = datasplit[0].strip("b'")
    humidity_dht = datasplit[-1]
    if (temperature_dht != ""):
        text_temp = temperature_dht
    
    
    return render_template("index.html", RAM_used = RAM_used, cpu_temp = cpu_temp, temp = text_temp, temp_city = temp_city)
    
# I will extend the index page to show the temperature & humidity history via graphics. Also I will be adding a videos
# section where I will be playing mp4 movie files.

# @app.route('/history/')
# def history():
    
#     return render_template("history.html")

# @app.route('/videos/')
# def videos():
    
#     return render_template("videos.html")

@app.route('/lights/')
def lights():
    
    return render_template("lights.html")

@app.route('/switch_lights', methods=['POST'])

def switch_lights():
    
    if request.form['btnlamp'] == "ON":
        ser.write(b"H_ON\n")
    elif request.form['btnlamp'] == "OFF":
        ser.write(b"H_OFF\n")
        
    return render_template("lights.html")

@app.route('/heater/')
def heater():
    
    return render_template("heater.html")

@app.route('/switch_heater', methods=['POST'])

def switch_heater():
    
    if request.form['btnheater'] == "ON":
        ser.write(b"ON\n")
    elif request.form['btnheater'] == "OFF":
        ser.write(b"OFF\n")
        
    return render_template("heater.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
