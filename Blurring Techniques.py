# BLURRING TECHNIQUES

import cv2 as cv
import numpy as np

img = cv.imread('photos/hadeen.png')
cv.imshow('Hadeen', img)

# Average Blur
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)




cv.waitKey(0)