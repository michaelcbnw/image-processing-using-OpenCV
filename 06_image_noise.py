'''
© Michael C B N W
'''
# import cv2 module
import cv2

# specify filename
filename = "chaplin.png"
# read filename
src = cv2.imread(filename)

# make a copy
image = src.copy()
# resize image
image = image[0:500, 0:500]
h = int(image.shape[0]/2)
w = int(image.shape[1]/2)
dim = (w, h)
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

# dilatation erosion
# dilate = cv2.dilate(image, (3, 3), iterations=10)
# erode = cv2.erode(dilate, (3, 3), iterations=10)

open = cv2.morphologyEx(image, cv2.MORPH_OPEN, (5, 5))
close = cv2.morphologyEx(open, cv2.MORPH_GRADIENT, (5, 5))
close *= 3
rotate = cv2.rotate(close, cv2.ROTATE_90_CLOCKWISE)
# show image
cv2.imshow("img", src)
# show deblurred
# cv2.imshow("img2", resized_image)

cv2.imshow('img3', rotate)

# press any key to continue...
cv2.waitKey(0)
