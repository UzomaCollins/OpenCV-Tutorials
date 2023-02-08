# BASIC FUNCTIONS IN OPENCV
import cv2 as cv

img = cv.imread('photos/hadeen.png')
cv.imshow('Hadeen', img)

# 1. Converting an image to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)
