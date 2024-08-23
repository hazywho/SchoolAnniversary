import serial

arduinoMega = serial.Serial('COM11', 9600) #arduino mega communication
def writeCoordsIntoMega(x,y):
    print(f"{y}{x}")
    arduino.write(f"{y}{x}".encode()) 