import cv2 as cv
import numpy as np

img = cv.imread('Photos/faces 1.jpeg')
cv.imshow('Face', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# Detect faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
# Draw rectangles around the faces
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
cv.imshow('Detected Faces', img)
cv.waitKey(0)