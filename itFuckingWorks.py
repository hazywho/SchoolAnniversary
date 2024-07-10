#sudo apt-get install python-spidev
#pip install RPLCD
#pip install adafruit-circuitpython-mcp3xxx
#pip install pyrebase
#pip install RPLCD
#pip install spidev
#sudo apt update
#sudo apt full-upgrade
#sudo raspi-config

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep
import smbus #For the LCD I2C
import time
import pyrebase

config = {
  "apiKey": "AIzaSyDCqcwzV_yQtJU2VTd0Gyut4p2Ntls5uts",
  "authDomain": "sis-sus.firebaseapp.com",
  "databaseURL": "https://sis-sus-default-rtdb.firebaseio.com",
  "projectId": "sis-sus",
  "storageBucket": "sis-sus.appspot.com",
  "messagingSenderId": "950036547603",
  "appId": "1:950036547603:web:636444af73e7d0b9f057e6",
  "measurementId": "G-Y3TX0QTEKJ"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Import LCD library and functions
from RPLCD.i2c import CharLCD

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def loop():
    for i in range(10):
        ph_buf[i] = analog_in_pH.voltage
        tds_buf[i] = analog_in_tds.voltage  # Read TDS sensor
        delay(30)

    ph_buf.sort()   # Sort pH buffer
    tds_buf.sort()  # Sort TDS buffer as well

    avgValue = sum(ph_buf[2:8]) / 6  # Calculate average pH value
    tds_avg = sum(tds_buf[2:8]) / 6  # Calculate average TDS value

    phValue = (float(avgValue) - 0) * (14 - 0) / (5 - 0) + 0
    phValue = round(phValue, 2)
    print(f"pH sensor = {phValue:.2f}")
    db.child("rasp3").update({"ph":phValue})

    tdsValue = (tds_avg - 0) * (2000 - 0) / (5 - 0) + 0
    tdsValue = round(tdsValue, 2)
    print(f"TDS sensor = {tdsValue:.2f}")
    db.child("rasp3").update({"tds":tdsValue})

    # Update LCD with pH and TDS values
    lcd.clear()
    lcd.write_string(f"pH: {phValue:.2f}            TDS: {tdsValue:.2f}")

    delay(500)

def delay(ms):
    time.sleep(ms / 1000.0)

#=================================================================================

calibration = 0.00  # pH calibration
tds_calibration = 1.23  # TDS calibration factor
ph_buf = [0] * 10
tds_buf = [0] * 10


# Initialize MCP3008 ADC
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D8)
mcp = MCP.MCP3008(spi, cs)

# Initialize analog input object for pH sensor connected to channel 0
analog_in_pH = AnalogIn(mcp, MCP.P0)  # Use channel 0 for pH sensor
analog_in_tds = AnalogIn(mcp, MCP.P1)  # Use channel 1 for tds sensor

# Initialize LCD on I2C bus
lcd = CharLCD('PCF8574', 0x27)

try:
    while True:
        loop()
        sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    pass


