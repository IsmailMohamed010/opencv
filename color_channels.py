import cv2 as cv
import numpy as np

img = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')    


cv.imshow('Original', img)

b,g,r = cv.split(img)
cv.imshow('Blue Channel', b)
cv.imshow('Green Channel', g)
cv.imshow('Red Channel', r)
print('Blue Channel Shape:', b.shape)
print('Green Channel Shape:', g.shape)
print('Red Channel Shape:', r.shape)


merged = cv.merge((b, g, r))
cv.imshow('Merged Image', merged)


blank = np.zeros(img.shape[:2], dtype=np.uint8)

blue = cv.merge((b, blank, blank))
cv.imshow('Blue Channel', blue)

green = cv.merge((blank, g, blank))
cv.imshow('Green Channel', green)

red = cv.merge((blank, blank, r))
cv.imshow('Red Channel', red)

cv.waitKey(0)