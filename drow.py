import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

blank[:] = 255, 0, 0  
#cv.imshow("Blank", blank)


#blank[100:200, 100:200] = 0, 0, 255
#cv.imshow("Blank", blank)

# Drow Regtangle
#cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
#cv.imshow("Rectangle", blank)


# Drow Circle
#cv.circle(blank, (250, 250), 40, (0, 255,0), thickness=2)
#cv.imshow("Circle", blank)

# Drow Line
#cv.line(blank, (0, 0), (500, 500), (0, 0, 255), thickness=3)
#cv.imshow("Line", blank)

# write text
cv.putText(blank, "OpenCV", (300, 300), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2)
cv.imshow("Text", blank)


img = cv.imread('Photos/wallpaperflare.com_wallpaper (1).jpg')
#cv.imshow("Sonic", img)


cv.waitKey(0)