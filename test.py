import pyfirmata
import pyfirmata.util
import time

global mouseX,mouseY
mouseX, mouseY=(0, 0)
#setup arduino
board = pyfirmata.Arduino('COM11') #change to uno com
pin=9
pin2=10
it2 = pyfirmata.util.Iterator(board=board)
it2.start()


megaPins = {
    61: board.get_pin('d:4:o'),
    62: board.get_pin('d:9:o'),
    63: board.get_pin('d:8:o'),
    64: board.get_pin('d:7:o'),
    65: board.get_pin('d:6:o'),
    66: board.get_pin('d:5:o')
}

switches = {key: 0 for key in megaPins.keys()} 
print(switches)
def reset_all_switches():
    global switches
    switches = {key: 0 for key in megaPins.keys()}
    for pin in megaPins.values():
        pin.write(0)  # Turn off all pins
    print("reset")

def toggle_switch(index):
    print(switches[index])
    if switches[index] == 0:
        megaPins[index].write(1)  # Turn on the pin
        switches[index] = 1
        print("on")
    else:
        megaPins[index].write(0)  # Turn off the pin
        switches[index] = 0 

def writeCoordsIntoMega(xy):
    for index in range(0,len(xy)-1,2):
        coords = int(xy[index:index+2])
        print("is",True if coords in megaPins else False)
        if coords in megaPins:
            print("toggled")
            toggle_switch(coords)
        elif coords == 99:
            
            reset_all_switches()
