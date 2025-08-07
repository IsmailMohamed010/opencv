import cv2 as cv
import numpy as np

img  = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')

cv.imshow('Original', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# laplacian gradient
lab = cv.Laplacian(gray, cv.CV_64F)
lab = np.uint8(np.absolute(lab))
cv.imshow('Laplacian', lab)

#sobel gradient
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_x = np.uint8(np.absolute(sobel_x))
cv.imshow('Sobel X', sobel_x)

sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_y = np.uint8(np.absolute(sobel_y))
cv.imshow('Sobel Y', sobel_y)


# applying bitwise or to combine the two sobel gradients
sobel_combined = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('Sobel Combined', sobel_combined)
# Canny edge detection
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)