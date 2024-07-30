import cv2
import serial
cap=cv2.VideoCapture(0)
global mouseX,mouseY
mouseX, mouseY=(0, 0)
arduino = serial.Serial('COM3', 9600)
cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
def write(event,mouseX,mouseY,flags,param):
    print(mouseX/640*180)
    print(mouseY/480*180)
    arduino.write(str(f"X{mouseX/640*180}Y{mouseY/480*180}").encode())
    
while True:
    ret, frame=cap.read() 
    cv2.imshow("frame", frame) 
    cv2.setMouseCallback(
        'frame', write
    )
    # cv2.setMouseCallback(
    #     'frame', lambda event, mouseX, mouseY, flags, param: 
    #     (print(mouseX/640*180),
    #     print(mouseY/480*180))
    # )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break