'''
© Michael C B N W
'''
# import cv2 module
import cv2

# specify filename
filename = "color_wheel.jpg"
# read filename
src = cv2.imread(filename)
# copy img to remain the original data
image = src.copy()
# resize image
# define height and width
height, width = image.shape[:2]
h = int(height / 2)  # change to INT for cut the .0
w = int(width / 2)
print(h, w, height, width)
image = cv2.resize(image, (h, w), interpolation=cv2.INTER_CUBIC)
# convert color space
'''
BGR/HSV/RGB/CIELAB/etc
https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html
'''
converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# show image source
cv2.imshow("img", src)
# show converted image
cv2.imshow("cvt", converted_image)
# press any key to continue...
cv2.waitKey(0)
