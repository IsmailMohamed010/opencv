import cv2 as cv
'''
# Read image
img = cv.imread('Photos/wallpaperflare.com_wallpaper (1).jpg')
# display the image
cv.imshow("Sonic", img)
'''

# read Video (use number for if you use webcam rather than a video file)
cap = cv.VideoCapture('Videos/100.mp4')

while True:
    # Read the frame from the video
    success, img = cap.read()
    
    # If the frame was not read successfully, break the loop
    if not success:
        break
    
    # Display the frame
    cv.imshow("Video Frame", img)
    
    # Wait for 1 ms and check if 'q' is pressed to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video capture object and close all OpenCV windows
cap.release()
cv.destroyAllWindows()