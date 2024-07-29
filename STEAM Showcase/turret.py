import cv2
import serial
cap=cv2.VideoCapture(0)
global mouseX,mouseY
mouseX, mouseY=(0, 0)
arduino = serial.Serial('COM3', 9600)
cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
    ret, frame=cap.read() 
    cv2.imshow("frame", frame) 
    cv2.setMouseCallback(
        'frame', lambda event, mouseX, mouseY, flags, param: 
        arduino.write(bytes(mouseX / (640 / 180),'utf-8')),
        arduino.write(bytes(mouseY / (480/180),'utf-8')))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break