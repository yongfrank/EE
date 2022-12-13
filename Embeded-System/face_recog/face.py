'''
Author: Frank Chu
Date: 2022-12-13 10:33:12
LastEditors: Frank Chu
LastEditTime: 2022-12-13 11:07:03
FilePath: /EE/Embeded-System/face_recog/face.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
import cv2

# Load the cascade classifier for detecting faces
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 机器学习人脸识别的算法 Cascade Classifier
# 它可以用来识别图像中的目标对象。它通过对图像进行多次分类，每一次分类都只考虑少量的信息，来确定图像中是否存在目标对象。
# A CascadeClassifier is a type of object detection algorithm used in computer vision tasks. It is a machine learning algorithm that is trained to detect objects in images or video by learning from labeled examples. The algorithm works by training a series of "weak" classifiers, each of which is able to slightly improve the detection performance, and then combining them to form a "strong" classifier that can effectively detect the objects in new images. This is done using a "cascade" of classifiers, where each classifier is trained to focus on a specific aspect of the image, and the
# haarcascade_frontalface_default 是一种计算机视觉算法，它用于检测人脸。
# https://www.cnblogs.com/zyly/p/9410563.html Haar(哈尔)特征分为三类：边缘特征、线性特征、中心特征和对角线特征，组合成特征模板。特征模板内有白色和黑色两种矩形，并定义该模板的特征值为白色矩形像素和减去黑色矩形像素和。Haar特征值反映了图像的灰度变化情况。例如：脸部的一些特征能由矩形特征简单的描述，如：眼睛要比脸颊颜色要深，鼻梁两侧比鼻梁颜色要深，嘴巴比周围颜色要深等。但矩形特征只对一些简单的图形结构，如边缘、线段较敏感，所以只能描述特定走向（水平、垂直、对角）的结构。
# 它是基于 Haar 特征的分类器，可以用来识别图像中的人脸，常用于人脸识别和人脸检测系统。
# 它通过训练大量的人脸图像，然后根据这些图像学习出人脸的特征，最后在新图像中使用这些特征来识别人脸。
# 目标检测（一）级联分类器 - 小岩子的文章 - 知乎
# https://zhuanlan.zhihu.com/p/405985394
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image and convert it to grayscale
image = cv2.imread('/Users/yongfrank/Developer/EE/Embeded-System/face_recog/face.jpeg')

# cv2.cvtColor() 是 OpenCV 中的一个图像颜色空间转换函数，它可以将图像从一种颜色空间转换为另一种颜色空间。
# 在这个函数的第二个参数中，cv2.COLOR_BGR2GRAY 表示将图像从 BGR 颜色空间转换为灰度颜色空间。
# 在计算机视觉任务中，灰度图像通常更容易处理，所以在进行图像处理之前，通常会将图像从 BGR 颜色空间转换为灰度颜色空间。
# 例如，在进行人脸检测时，将图像转换为灰度图像可以提高检测的准确性。
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
# 在这段代码中，faces 变量表示一个列表，其中包含检测到的人脸的坐标信息。
# face_cascade.detectMultiScale() 是一个人脸检测函数，它可以用来检测图像中的人脸。
# 它的第一个参数是要检测的图像，第二个参数是缩放因子，第三个参数是最小邻居数。
# 缩放因子指的是在检测过程中，每次缩小图像的比例。它的值越大，检测的速度越快，但是精度可能会下降。
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Print the number of faces detected
print('Number of faces detected:', len(faces))

# Draw a rectangle around each face
for (x, y, w, h) in faces:
    # BGR 颜色空间
    # 为什么 OpenCV 中使用的是 BGR 颜色空间而不是 RGB 颜色空间，
    # 这主要是因为 BGR 颜色空间与计算机显示器的颜色空间匹配得更好，
    # 它们的分量顺序相同，这样可以更方便地进行图像处理。
    # 因此，OpenCV 中选择使用 BGR 颜色空间。
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Save the resulting image
cv2.imwrite('image_with_faces.jpg', image)