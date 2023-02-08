# RESIZING AND RESCALING

import cv2 as cv

def rescaleFrame(frame):
    scale_width = 0.1
    scale_height = 0.3
    width = int(frame.shape[0] * scale_width)
    height = int(frame.shape[1] * scale_height)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('videos/v2.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
