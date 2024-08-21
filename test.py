import cv2


# make a copy of the original image
imageFilledCircle = img.copy()
# define center of the circle 
circle_center = (415,190)
# define the radius of the circle
radius =100
# draw the filled circle on input image
cv2.circle(imageFilledCircle, circle_center, radius, (255, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
# display the output image 
cv2.imshow('Image with Filled Circle',imageFilledCircle)
cv2.waitKey(0)