# IMAGE ROTATION

import cv2 as cv
import numpy as np

img = cv.imread('photos/hadeen.png')
cv.imshow('Hadeen', img)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)

        return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0, )
cv.imshow('Flipped', flip)

# Cropping
cropped = img[50:100, 100:200]
cv.imshow('Cropped', cropped)

cv.waitKey(0)