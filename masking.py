import cv2 as cv
import numpy as np

img = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype=np.uint8)

mask = cv.circle(blank, (img.shape[1]//2 -50, img.shape[0]//2), 150, 255, -1)
cv.imshow('Mask', mask)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_img)

# Creating a rectangle mask
rectangle_mask = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('Rectangle Mask', rectangle_mask)

masked_rectangle = cv.bitwise_and(img, img, mask=rectangle_mask)
cv.imshow('Masked Rectangle Image', masked_rectangle)
cv.waitKey(0)