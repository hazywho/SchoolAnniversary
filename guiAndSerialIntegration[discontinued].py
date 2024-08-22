import random
import cv2
import serial
import numpy as np

#setup video and transmission
cap=cv2.VideoCapture(0)
global mouseX,mouseY
mouseX, mouseY=(0, 0)
arduino = serial.Serial('COM3', 9600)
cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) 

#setup board
board_size_cm = 120
spacing_cm = 20
start_cm = 10
num_arrays = (board_size_cm - start_cm) // spacing_cm #10
buttons = []

def mouseReadWrite(event,x,y,flags,param):
    print(mouseX/640*180)
    print(mouseY/480*180)
    arduino.write(str(f"X{mouseX/640*180}Y{mouseY/480*180}").encode())
    #checks mouse left button down condition
    if event == cv2.EVENT_LBUTTONDOWN and frame[y,x,2]==255: 
        print("did something")
        
        check_level()

def generate_random_position():
    x = start_cm + random.randint(0, num_arrays) * spacing_cm
    y = start_cm + random.randint(0, num_arrays) * spacing_cm
    return (x, y)
for _ in range((num_arrays+1) * (num_arrays+1)): # Draw the LED arrays
    x, y = generate_random_position()
    while (x, y) in [pos for _, pos, _ in buttons]:
        x, y = generate_random_position()

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
def show_buttons(frame,array=xylist):
    coords = []
    for circle_center in coords:
        cv2.circle(frame, circle_center, 10, (0, 0, 255), thickness=-0.5, lineType=cv2.LINE_AA) 

def clear_buttonStates():

# Function to finish the game
def finish_game():
    for _ in range(3):
        #display you win
        clear_buttonStates()

level = 1
score = 0

while True:
    ret, frame=cap.read() 

    cv2.imshow("frame", frame) 
    cv2.setMouseCallback(
        'frame', mouseReadWrite
    )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




    
# make a copy of the original image
imageFilledCircle = img.copy()
# define center of the circle 

# define the radius of the circle
radius =100
# draw the filled circle on input image
cv2.circle(imageFilledCircle, circle_center, radius, (255, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
# display the output image 
cv2.imshow('Image with Filled Circle',imageFilledCircle)
cv2.waitKey(0)