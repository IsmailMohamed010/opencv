import cv2 as cv

# resize for image.
img  = cv.imread('Photos/wallpaperflare.com_wallpaper (1).jpg')
cv.imshow("Sonic", img)

cv.waitKey(0)


# Function to rescale the image
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Rescale the image
rescaled_image = rescaleFrame(img, scale=0.75)
cv.imshow("Rescaled Image", rescaled_image)
cv.waitKey(0)



# resize for video.
cap = cv.VideoCapture('Videos/100.mp4')

while True:
    # Read the frame from the video
    success, img = cap.read()
    
    img_scaled = rescaleFrame(img, scale=0.5)
    # If the frame was not read successfully, break the loop
    if not success:
        break
    
    # Display the frame
    cv.imshow("Video Frame", img_scaled)
    
    # Wait for 1 ms and check if 'q' is pressed to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


def changeres(width, height):
    # for live video
    cap.set(3, width)  # Set width
    cap.set(4, height)  # Set height