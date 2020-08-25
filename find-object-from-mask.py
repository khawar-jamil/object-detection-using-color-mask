import cv2

# Mask values of the object to be detected
min_blue=91  
min_green=21 
min_red=49
max_blue=111 
max_green=255 
max_red=255

# file path of the video in which we want to find object
video_path = './data/cup.mov'

camera = cv2.VideoCapture(video_path)

if not camera.isOpened():
    camera.open(video_path)
    
if camera.isOpened():
    print("Device Opened\n")
else:
    print("Failed to open Device\n")


while True:
    # reading single frame of the video
    ret, frame = camera.read()
    # if no more frame is found we break out of the loop
    if not ret:
        break
    
    # converting image into HSV color space as opencv reads image in BGR color model by default
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #getting the mask image from the HSV image using threshold values
    mask = cv2.inRange(hsv_frame, (min_blue, min_green, min_red), (max_blue, max_green, max_red))
    #extracting the contours of the object
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #sorting the contour based of area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    if contours:
        #if any contours are found we take the biggest contour and get bounding box
        (x_min, y_min, box_width, box_height) = cv2.boundingRect(contours[0])
        #drawing a rectangle around the object with 15 as margin
        cv2.rectangle(frame, (x_min - 15, y_min -15),
                      (x_min + box_width + 15, y_min + box_height + 15),
                      (0,255,0), 4)
        
    #showing each frame of the video 
    cv2.imshow('frame',frame)
    key = cv2.waitKey(5)
    # waiting for q key to be pressed and then breaking
    if key == ord('q'):
        break
# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()            