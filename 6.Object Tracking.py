import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    # Threshold the HSV image to get only blue colors
    # mask = cv.inRange(hsv, lower_blue, upper_blue)
    mask = cv.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()