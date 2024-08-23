import matplotlib.pyplot as plt
import numpy as np
import random
import serial

global mouseX,mouseY
mouseX, mouseY=(0, 0)
arduino = serial.Serial('COM3', 9600)
arduinoMega = serial.Serial('COM11', 9600) #arduino mega communication
def write(mouseX,mouseY):
    resolution = (120,120)
    print(180-(mouseX/(120+resolution[0])*180))
    print(mouseY/resolution[1]*180)
    arduino.write(str(f"X{180-(mouseX/resolution[1]*180)}Y{mouseY/resolution[0]*180}").encode()) #set resolution

def writeCoordsIntoMega(x,y):
    print(f"{y}{x}")
    arduinoMega.write(f"{y}{x}".encode()) 

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
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')
        write(event.xdata,event.ydata)
        
def onclick(event):
    global score
    for button, pos, state in buttons:
        if button.contains(event)[0]:
            if state:
                button.set_facecolor('white')
                buttons[buttons.index((button, pos, state))] = (button, pos, False)
                sendX=int(((pos[0]-10)/20)+1)
                sendY=int((6-(((pos[1]-10)/20)+1))+1)
                writeCoordsIntoMega(x=sendX,y=sendY)
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
    writeCoordsIntoMega(x=9,y=9)
    num_buttons_to_show = int(len(buttons) * percentage)
    random_buttons = random.sample(buttons, num_buttons_to_show)
    for button, pos, state in buttons:
        button.set_facecolor('white')
        buttons[buttons.index((button, pos, state))] = (button, pos, False)
    for button, pos, state in random_buttons:
        button.set_facecolor('red')
        sendX=int(((pos[0]-10)/20)+1)
        sendY=int((6-(((pos[1]-10)/20)+1))+1)
        writeCoordsIntoMega(x=sendX,y=sendY)
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

