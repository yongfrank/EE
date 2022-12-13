'''
Author: Frank Chu
Date: 2022-12-13 11:09:03
LastEditors: Frank Chu
LastEditTime: 2022-12-13 11:11:27
FilePath: /EE/Embeded-System/python/deteceFace.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
import cv2

# Create a background subtractor object
bs = cv2.createBackgroundSubtractorMOG2()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture video from your Mac's camera
cap = cv2.VideoCapture(0)

while True:
    # Read the next frame from the video stream
    _, frame = cap.read()

    # Use the background subtractor to detect motion in the frame
    fgmask = bs.apply(frame)

    # Convert the motion mask to a binary image
    # thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]

    # Find the contours in the binary image
    # contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
    # BGR 颜色空间
    # 为什么 OpenCV 中使用的是 BGR 颜色空间而不是 RGB 颜色空间，
    # 这主要是因为 BGR 颜色空间与计算机显示器的颜色空间匹配得更好，
    # 它们的分量顺序相同，这样可以更方便地进行图像处理。
    # 因此，OpenCV 中选择使用 BGR 颜色空间。
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    
    # # Find the contour with the largest area
    # main_contour = None
    # main_contour_area = 0
    # for c in contours:
    #     area = cv2.contourArea(c)
    #     if area > main_contour_area:
    #         main_contour = c
    #         main_contour_area = area

    # # Draw a contour around the main moving object
    # if main_contour is not None:
    #     # cv2.drawContours(frame, [main_contour], 0, (0, 255, 0), 2)
    #     x, y, w, h = cv2.boundingRect(main_contour)
    #     side = max(w, h)
    #     cv2.rectangle(frame, (x, y), (x+side, y+side), (0, 255, 0), 2)


    # Display the original frame and the contour
    cv2.imshow('Frame', frame)
    # cv2.imshow('Contours', thresh)

    # Check if the user pressed the 'q' key
    key = cv2.waitKey(30) & 0xff
    if key == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
