# SHAPES AND TEXT ON IMAGES

from pickletools import uint8
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (250, 250), 80, (0, 255, 0), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (100, 250), (0, 255, 0), thickness=3)
cv.imshow('Line', blank)

# 5. Write text on image
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)


img = cv.imread('photos/hadeen.png')
cv.imshow('Picture', img)

cv.waitKey(0)