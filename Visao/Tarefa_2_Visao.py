import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    _, img = video.read()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blue = np.array([101, 50, 38])
    BLUE = np.array([110, 255, 255])

    mask = cv.inRange(hsv, blue, BLUE)

    res = cv.bitwise_and(img, img, mask= mask)
    img[np.where ((img == res).all(axis=2))] = [0, 0, 255]
    cv.imshow("Change", img)
    cv.imshow("mascara", mask)
    if cv.waitKey(1) == ord ('0'):
        break
cv.destroyAllWindows()