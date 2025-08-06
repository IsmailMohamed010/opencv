import cv2 as cv
import numpy as np


blank = np.zeros((400, 400), dtype=np.uint8)


regtangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('Rectangle', regtangle)

cercile = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow('Circle', cercile)

# bitwise AND
bitwise_and = cv.bitwise_and(regtangle, cercile)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(regtangle, cercile)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(regtangle, cercile)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not_rectangle = cv.bitwise_not(regtangle)
cv.imshow('Bitwise NOT Rectangle', bitwise_not_rectangle)

cv.waitKey(0)