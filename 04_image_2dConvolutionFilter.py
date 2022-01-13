'''
© Michael C B N W
'''
# import cv2, numpy
import cv2
import numpy as np

# specify filename
filename = "redoxon.jpg"
# read filename
src = cv2.imread(filename)

# copy the image
image = src.copy()
# resize the image
height, width = image.shape[:2]
h, w = int(height/2), int(width/2)
print(image.shape)
image = cv2.resize(
    image, (w, h), interpolation=cv2.INTER_CUBIC)
print(image.shape)

# unsharp kernel
unsharp = [[1, 4, 6, 4, 1],
           [4, 16, 24, 16, 4],
           [6, 24, -476, 24, 6],
           [4, 16, 24, 16, 4],
           [1, 4, 6, 4, 1], ]
ngawur = [[1, 0, 1],
          [-5, 0, 5],
          [1, 0, 1], ]

# define kernel
kernel = -np.array(ngawur, np.float32)
# 2D convolution
dst = cv2.filter2D(image, -1, kernel)
# show image
cv2.imshow("img", image)
# show image
cv2.imshow("dst", dst)
# press any key to continue...
cv2.waitKey(0)
