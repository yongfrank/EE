'''
Author: Frank Chu
Date: 2022-12-06 12:10:14
LastEditors: Frank Chu
LastEditTime: 2022-12-06 13:11:48
FilePath: /EE/Embeded-System/python/lab06T1.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
import cv2 

# cv2.VideoCapture(0), 0 is the default camera
cap = cv2.VideoCapture(0)

print("VideoCapture is opened?", cap.isOpened)

while(True):

    # _, frame = cap.read()
    _, frame = cap.read() 
    center = (frame.shape[1]//2, frame.shape[0]//2)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.circle(frame, center=(200, 200), radius=100, color=(0,0,255))

    # Display the original frame and the contour
    # cv2.imshow('Frame', frame)
    # cv2.imshow('Contours', thresh)
    cv2.namedWindow("aaa",0) 
    cv2.imshow("aaa", frame)

    # Check if the user pressed the 'q' key
    # key = cv2.waitKey(30) & 0xff
    # if key == ord('q'):
    #     break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()
