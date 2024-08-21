import math
y2=0
x2=0
y1=180
x1=180
try:
    angle = round(math.atan2((y2-y1),(x2-x1))*180/3.141592653589)
    print(angle)
except ZeroDivisionError:
    print(0)
