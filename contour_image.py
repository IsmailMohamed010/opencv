import cv2 as cv
import numpy as np

img = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')
cv.imshow('Sonic', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
canny = cv.Canny(img, 125, 175)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
blank = np.zeros(img.shape, dtype='uint8')

cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)