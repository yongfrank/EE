'''
Author: Frank Chu
Date: 2022-12-06 12:10:14
LastEditors: Frank Chu
LastEditTime: 2022-12-13 06:50:47
FilePath: /EE/Embeded-System/python/lab06T1.py
Description: https://youtu.be/dCSZvP5IAqc

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
import cv2 
import numpy as np
import cv2

# Load the video file
video = cv2.VideoCapture(0)

# Load the image that you want to overlay on top of the video
overlay_img = cv2.imread("/Users/yongfrank/Developer/EE/Embeded-System/python/zstu.jpg")

# Get the dimensions of the video frame and the overlay image
video_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
video_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
overlay_width = overlay_img.shape[1]
overlay_height = overlay_img.shape[0]

# Set the starting position for the overlay image (top-left corner)
# You can adjust this to place the image at different positions
x = 0
y = 0

# Loop over each frame of the video
while True:
    # Grab the current frame
    ret, frame = video.read()

    # If we have reached the end of the video, break out of the loop
    if not ret:
        break

    # Resize the overlay image to match the dimensions of the frame
    # This is important because the dimensions of the frame may be different
    # from the dimensions of the overlay image
    resized_overlay = cv2.resize(overlay_img, (overlay_width, overlay_height))

    # Overlay the resized image on top of the frame
    frame[y:y+overlay_height, x:x+overlay_width] = resized_overlay

    # Show the frame
    cv2.imshow("Video with Overlay", frame)

    # Check if the user has pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()


# # cv2.VideoCapture(0), 0 is the default camera
# capture_of_camera = cv2.VideoCapture(0)
# capture_of_camera.set(cv2.CAP_PROP_FPS, 30)

# print("VideoCapture is opened?", capture_of_camera.isOpened)

# img_zstu = cv2.imread('/Users/yongfrank/Developer/EE/Embeded-System/python/zstu.png')

# # Set the frame width and height
# # capture_of_camera.set(cv2.CAP_PROP_FRAME_WIDTH, img_zstu.shape[1])
# # capture_of_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, img_zstu.shape[0])


# while(True):
#     # _, frame = cap.read()
#     # Frame Size, Width
#     # https://stackoverflow.com/questions/28773186/what-does-ret-and-frame-mean-here
#     # ret is a boolean variable that returns true if the frame is available. return value
#     ret, frame = capture_of_camera.read() 
    
#     # Converts an image from one color space to another.
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
#     zstuLogo = cv2.cvtColor(img_zstu, cv2.COLOR_BGR2BGRA)
#     # zstuLogo = img_zstu
    
#     # Building Overlay
#     frame_h, fram_w, frame_c = frame.shape
#     overlay = np.zeros((frame_h, fram_w, 4), dtype='uint8')
#     zstuLogo_h, zstuLogo_w, zstuLogo_c = zstuLogo.shape
#     for i in range(0, zstuLogo_h):
#         for j in range(0, zstuLogo_w):
#             if zstuLogo[i, j][3] != 0:
#                 overlay[i + 10, j + 10] = zstuLogo[i, j]
    
#     cv2.addWeighted(overlay, 1, frame, 1, 0, frame)
#     cv2.addWeighted()
#     cv2.imshow("Video Broadcasting", frame)

#     # Check if the user pressed the 'q' key
#     # key = cv2.waitKey(30) & 0xff
#     # if key == ord('q'):
#     #     break
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     ret, frame = capture_of_camera.read()

# capture_of_camera.release() 
# cv2.destroyAllWindows()


#     # center = (frame.shape[1] // 2, frame.shape[0] // 2)
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
#     # cv2.circle(frame, center=(200, 200), radius=100, color=(0,0,255))
#     # Display Image
    
#     # Display the original frame and the contour
#     # cv2.imshow('Frame', frame)
#     # cv2.imshow('Contours', thresh)
#     # cv2.namedWindow("Video Recoding",0) 