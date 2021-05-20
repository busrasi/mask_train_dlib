#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:03:48 2021

@author: busrasirin
"""
import dlib
import cv2
import os




detector = dlib.simple_object_detector("mask_detect_v2.svm")


testImagesPath = "test_images"
testImages = os.listdir(testImagesPath)

for image in testImages:
   # frame = cv2.imread(testImagesPath+"/"+image)
    dlibFrame = dlib.load_rgb_image("/Users/busrasirin/Desktop/my_train_mask/train/test_images/"+image)
    frame = cv2.imread("/Users/busrasirin/Desktop/my_train_mask/train/test_images/"+image)
   #frame = cv2.resize(frame, (1920,1080))
    
    rectangle = detector(dlibFrame)
   



    left = rectangle[0].left()
    top = rectangle[0].top()
    right = rectangle[0].right()
    bottom = rectangle[0].bottom()

    x = left
    y = top
    w = right - x
    h = bottom - y

    print(x, y, w, h)

    cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0,0,255))
    #frame = cv2.resize(frame, (825, 540))
    cv2.imshow("Detected",frame)
    cv2.waitKey(0)