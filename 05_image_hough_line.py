'''
© Michael C B N W
'''
# import cv2, math, numpy
import cv2
import math
import numpy as np

# filename
filename = "sudoku.jpg"
# read filename
src = cv2.imread(filename)

# copy image
image = src.copy()
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur the image
blur = cv2.GaussianBlur(image, (5, 5), 0)
# crate canny image
canny = cv2.Canny(blur, 50, 200, None, 3)

lines = cv2.HoughLines(canny, 1, np.pi / 180, 150, None, 0, 0)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(image, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)


# linesP = cv2.HoughLinesP(canny, 1, np.pi / 180, 50, None, 50, 10)

# if linesP is not None:
#     for i in range(0, len(linesP)):
#         l = linesP[i][0]
#         cv2.line(image, (l[0], l[1]), (l[2], l[3]),
#                  (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow("Source", src)
cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", image)
# cv2.imshow("Detected Lines (in red) - Probabilistic Line Transform", image)
# line = cv2.HoughLinesP(canny, )
# show the image
cv2.imshow("source", src)
# show the canny image
cv2.imshow("canny", canny)

# press any key to continue
cv2.waitKey(0)
