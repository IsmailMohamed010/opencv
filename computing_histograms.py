import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')
cv.imshow('Original', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray)

mask = cv.circle(np.zeros(img.shape[:2], dtype=np.uint8), (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
plt.plot(gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])
plt.show()


# Color Histogram
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.title('Color Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)