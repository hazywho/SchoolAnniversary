import pyfirmata
import pyfirmata.util
import matplotlib.pyplot as plt
import numpy as np
import random
import time 

global mouseX,mouseY
mouseX, mouseY=(0, 0)
#setup arduino
board = pyfirmata.Arduino('COM11') #change to uno com
megaBoard = pyfirmata.Arduino('COM3') #change to uno com
pin=9
pin2=10
it = pyfirmata.util.Iterator(board=board)
it2 = pyfirmata.util.Iterator(board=megaBoard)
it.start()
it2.start()
board.digital[pin].mode=pyfirmata.SERVO
board.digital[pin2].mode=pyfirmata.SERVO

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

def write(mouseX,mouseY):
    resolution = (120,120)
    angle = 30
    # print(mouseX/resolution[0]*angle)
    # print(mouseY/resolution[1]*angle)
    board.digital[pin].write(int(mouseX/resolution[0]*angle))
    board.digital[pin2].write(int(mouseY/resolution[1]*angle))

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
time.sleep(5)
#setup board
board_size_cm = 120
spacing_cm = 20
start_cm = 10
num_arrays = (board_size_cm - start_cm) // spacing_cm + 1
fig, ax = plt.subplots(figsize=(10, 10))
buttons = []

# Function to generate a random position for a button
def generate_random_position():
    x = start_cm + random.randint(0, num_arrays - 1) * spacing_cm
    y = start_cm + random.randint(0, num_arrays - 1) * spacing_cm
    return (x, y)

# Draw the LED arrays
for _ in range(num_arrays * num_arrays):
    x, y = generate_random_position()
    while (x, y) in [pos for _, pos, _ in buttons]:
        x, y = generate_random_position()
    # Draw a single button
    button = plt.Rectangle((x, y), 4, 4, edgecolor='red', facecolor='white', picker=True)
    ax.add_patch(button)
    buttons.append((button, (x, y), False))  # Store the button, its position, and its state

# Set the board limits
ax.set_xlim(0, board_size_cm)
ax.set_ylim(0, board_size_cm)

# Set the ticks
ax.set_xticks(np.arange(0, board_size_cm + spacing_cm, spacing_cm))
ax.set_yticks(np.arange(0, board_size_cm + spacing_cm, spacing_cm))

# Add grid
ax.grid(True)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Initialize level and score
level = 1
score = 0

def update_display():
    ax.set_title(f'Level {level}, Score: {score}')
    fig.canvas.draw_idle()

def on_move(event):
    if event.inaxes:
        # print(f'data coords {event.xdata} {event.ydata},',
        #       f'pixel coords {event.x} {event.y}')
        write(120-event.xdata,120-event.ydata)
        
def onclick(event):
    global score
    for button, pos, state in buttons:
        if button.contains(event)[0]:
            if state:
                button.set_facecolor('white')
                buttons[buttons.index((button, pos, state))] = (button, pos, False)
                sendX=int(((pos[0]-10)/20)+1)
                sendY=int(((pos[1]-10)/20)+1)

                writeCoordsIntoMega(str(sendY)+str(sendX))

                score += 1
                update_display()
                fig.canvas.draw_idle()
                check_level()

# Function to check if the level is complete
def check_level():
    global level
    remaining_buttons = sum(1 for _, _, state in buttons if state)
    if remaining_buttons == 0:
        level += 1
        if level > 5:
            finish_game()
        else:
            show_buttons(level / 5.0)  # Increase the percentage of visible buttons as the level increases

# Function to show a percentage of buttons
def show_buttons(percentage):
    writeCoordsIntoMega("99")
    num_buttons_to_show = int(len(buttons) * percentage)
    random_buttons = random.sample(buttons, num_buttons_to_show)
    for button, pos, state in buttons:
        button.set_facecolor('white')
        buttons[buttons.index((button, pos, state))] = (button, pos, False)
    for button, pos, state in random_buttons:
        sendX=int(((pos[0]-10)/20)+1)
        sendY=int(((pos[1]-10)/20)+1)

        writeCoordsIntoMega(str(sendY)+str(sendX))#write into mega

        button.set_facecolor('red')
        buttons[buttons.index((button, pos, state))] = (button, pos, True)

    fig.canvas.draw_idle()

# Function to finish the game
def finish_game():
    for _ in range(3):
        for button, pos, state in buttons:
            button.set_facecolor('green')
        fig.canvas.draw_idle()
        plt.pause(0.5)
        for button, pos, state in buttons:
            button.set_facecolor('red')
        fig.canvas.draw_idle()
        plt.pause(0.5)
    plt.close()

# Initialize the game
show_buttons(0.2)  # Start with 20% of buttons visible
update_display()

# Connect the function to the click event
cid = fig.canvas.mpl_connect('button_press_event', onclick)
binding_id = plt.connect('motion_notify_event', on_move)
# Show the plot
plt.title('The Game')
plt.xlabel('cm')
plt.ylabel('cm')
plt.show()