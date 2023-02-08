# RESIZING AND RESCALING 
import cv2 as cv

img = cv.imread('photos/hadeen.png')

def rescaleFrame(frame, scale= 1.0):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  

resized_img = rescaleFrame(img)
cv.imshow('Picture', resized_img)

cv.waitKey(0)