# object-detection-using-color-mask
A simple object detection application to detect objects in a video based on color information of an object


## Algorithm
- Load the image
- Convert the image into HSV color Model.
- Identify the min and max values for blue, green and red channel(threshold values)
- Read the image or frame in which we want to detect the object
- Convert the image/frame to HSV color model 
- Extract the mask by passing our threshold values for the BGR channel.
- Find  the contour of the object on the mask.
- Pick the largest contour.
- Draw the bounding box on the image using the contour information. 
- Display the image/frame.

## Pre-Checks
- make sure you have  opencv installed
- create a data folder 
- copy image and video of object in data folder
- update image and video paths

## Execution
- run find-mask.py to get the mask values
- copy the mask values and update it in find-object-from-mack.py
- run find-object-from-mack.py
