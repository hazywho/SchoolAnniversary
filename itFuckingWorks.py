#sudo apt-get install python-spidev
#pip install RPLCD
#pip install adafruit-circuitpython-mcp3xxx
#pip install pyrebase
#pip install RPLCD
#pip install spidev
#sudo apt update
#sudo apt full-upgrade
#sudo raspi-config
#source venv/bin/activate
# Import library and functions
import serial
import keyboard
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
import glob
import os
import gradio as gr

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    temp_c=0
    temp_f=0
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.1)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c
    
#define static var
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
lcd = CharLCD('PCF8574', 0x27)
global temp,turbidity,Tds
stopCode=False
try:
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1) #edit serial port here
except Exception:
    raise Exception("port incorrect or not connected. Try ls /dev/tty* to search for ports.")

def stop():
    global stopCode
    stopCode=True
    return "Stopped"

def run():
    x=0
    Tds=0
    turbidity=0
    temp=0
    while True:
        #temperature
        temp = read_temp()
        val=f"temp: {temp}"
        lcd.clear()
        lcd.write_string(val)
        #TDS and turbidity
        data = arduino.readline()
        print(data)
        data=data.decode()
        if data:
            if x==0:
                x=1
                turbidity= data #turbid
            else:
                x=0
                Tds = data #tds
        yield f"Temperature: {temp}. Turbidity: {turbidity}Total dissolved solid: {Tds}"
        if stopCode==True:
            time.sleep(0.3)
            print("terminated")
            break
        
#=================================================================================

with gr.Blocks() as demo:
    btn1 = gr.Button(value="run")
    btn2 = gr.Button(value="stop")
    display = gr.Textbox(value="",label="Outputs")
    btn1.click(fn=run,outputs=display)
    btn2.click(fn=stop,outputs=display)

demo.launch()




