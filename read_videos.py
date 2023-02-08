# READING VIDEOS IN OPENCV

import cv2 as cv

capture = cv.VideoCapture('videos/v2.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()