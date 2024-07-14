import serial 
import time 
import keyboard
x=0
arduino = serial.Serial(port='COM9', baudrate=9600, timeout=.1)
global stop 
stop=False
def run():
    while True:
        data = arduino.readline()
        data=data.decode()
        if data:
            if x==0:
                x=1
                turbidity= float(data)
            else:
                x=0
                Tds = float(data)

        if stop==True:
            time.sleep(0.4)
            print("terminated")
            break
        yield f"Turbidity: {turbidity}. Total dissolved solid: {Tds}"

def stop():
    stop=True
    return "Stopped"