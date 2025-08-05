import cv2  as cv
import numpy as np

img = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')

cv.imshow('Sonic', img)


# translation image
def translate(img,x,y):
    transmetric = np.float32([[1,0,x],[0,1,y]])
    dimansions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmetric, dimansions)


# -X --> Left not right
# -Y --> Up not down
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


# rotation image
def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (w // 2, h // 2)
    
    rotMetric = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimansions = (w, h)
    return cv.warpAffine(img, rotMetric, dimansions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_reversed = rotate(rotated, -45)
cv.imshow('Rotated_reversed', rotated_reversed)

# resize image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# flip image
flipped = cv.flip(img, 1)  # 0 for vertical, 1 for horizontal, -1 for both
cv.imshow('Flipped', flipped)


# crop image
cropped = img[50:200, 200:400]  # y1:y2, x1:x2
cv.imshow('Cropped', cropped)

cv.waitKey(0)