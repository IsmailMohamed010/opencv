import cv2 as cv

img = cv.imread('Photos/sonic-sonic-the-hedgehog-tails-character-fox-sega-hd-wallpaper-preview.jpg')
cv.imshow("Sonic", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# Blur the image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blurred Image", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated Image", dilated)

# Eroding the image
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded Image", eroded)

# Release the video capture object and close all OpenCV windows
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized Image", resized)

# crop the image
cropped = img[50:200, 200:400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)