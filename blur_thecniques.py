import cv2 as cv
import numpy as np

img = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')

cv.imshow('Original', img)


# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Averaged Image', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Gaussian Blurred Image', gaussian)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blurred Image', median)

# Bilateral Filter
bilateral = cv.bilateralFilter(img, 10, 35, 25) 
cv.imshow('Bilateral Filtered Image', bilateral)


cv.waitKey(0)