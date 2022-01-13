'''
© Michael C B N W
'''
# import cv2 module
import cv2

# specify filename
filename = "sudoku.jpg"
# read filename
src = cv2.imread(filename)

# show image
cv2.imshow("img", src)
# press any key to continue...
cv2.waitKey(0)
