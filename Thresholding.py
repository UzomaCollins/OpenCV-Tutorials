import cv2 as cv
import numpy as np

img = cv.imread('photos/hadeen.png')
cv.imshow('Hadeen', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold_Inverse', thresh_inv)

# Adaptive Thresholding
Adaptive_thresholding = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv.THRESH_BINARY, 11, 3)
cv.imshow('Simple Threshold', Adaptive_thresholding)



cv.waitKey(0)