import cv2 as cv

img = cv.imread('photos/hadeen.png')

cv.imshow('Picture', img)

cv.waitKey(0)