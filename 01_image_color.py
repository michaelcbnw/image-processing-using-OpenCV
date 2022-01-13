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
# convert color space to which your desired
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
