
import pyfirmata
import pyfirmata.util
import matplotlib.pyplot as plt
import numpy as np
import random
import time

megaBoard = pyfirmata.ArduinoMega('COM3') #change to uno com
pin=9
pin2=10

it2 = pyfirmata.util.Iterator(board=megaBoard)
it2.start()
#delcare mega pins here, change number infront to change which actiavtes, format = yx
megaPins = {
    11: megaBoard.get_pin('d:26:o'),
    16: megaBoard.get_pin('d:27:o'),
    15: megaBoard.get_pin('d:24:o'),
    14: megaBoard.get_pin('d:25:o'),
    13: megaBoard.get_pin('d:22:o'),
    12: megaBoard.get_pin('d:23:o'),
    21: megaBoard.get_pin('d:32:o'),
    26: megaBoard.get_pin('d:33:o'),
    25: megaBoard.get_pin('d:30:o'),
    24: megaBoard.get_pin('d:31:o'),
    23: megaBoard.get_pin('d:28:o'),
    22: megaBoard.get_pin('d:29:o'),
    31: megaBoard.get_pin('d:38:o'),
    36: megaBoard.get_pin('d:39:o'),
    33: megaBoard.get_pin('d:34:o'),
    34: megaBoard.get_pin('d:37:o'),
    35: megaBoard.get_pin('d:36:o'),
    32: megaBoard.get_pin('d:35:o'),
    41: megaBoard.get_pin('d:44:o'),
    46: megaBoard.get_pin('d:45:o'),
    45: megaBoard.get_pin('d:42:o'),
    44: megaBoard.get_pin('d:43:o'),
    43: megaBoard.get_pin('d:40:o'),
    42: megaBoard.get_pin('d:41:o'),
    51: megaBoard.get_pin('d:50:o'),
    56: megaBoard.get_pin('d:51:o'),
    55: megaBoard.get_pin('d:48:o'),
    54: megaBoard.get_pin('d:49:o'),
    53: megaBoard.get_pin('d:46:o'),
    52: megaBoard.get_pin('d:47:o'),
    61: megaBoard.get_pin('d:4:o'),
    62: megaBoard.get_pin('d:9:o'),
    63: megaBoard.get_pin('d:8:o'),
    64: megaBoard.get_pin('d:7:o'),
    65: megaBoard.get_pin('d:6:o'),
    66: megaBoard.get_pin('d:5:o')
}

switches = {key: 0 for key in megaPins.keys()} 

def reset_all_switches():
    global switches
    switches = {key: 0 for key in megaPins.keys()}
    for pin in megaPins.values():
        pin.write(0)  # Turn off all pins



def toggle_switch(index):
    if switches[index] == 0:
        megaPins[index].write(1)  # Turn on the pin
        switches[index] = 1
    else:
        megaPins[index].write(0)  # Turn off the pin
        switches[index] = 0 

def writeCoordsIntoMega(xy):
    print(f"key: {xy}")
    for index in range(0,len(xy)-1,2):
        coords = int(xy[index:index+2])
        # print(f"FUCKING COORDS {coords}, type: {type(coords)}")
        # print("is",True if coords in megaPins.keys() else False, f"because {megaPins.keys()}")
        if coords in megaPins:
            toggle_switch(coords)
        elif coords == 99:
            reset_all_switches()
            print("reset")

writeCoordsIntoMega("64")