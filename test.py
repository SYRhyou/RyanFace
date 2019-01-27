import cv2, dlib, sys
import numpy as np

cap = cv2.VideoCapture('samples/hj.mp4')

while True:
    ret, img = cap.read()
    if not ret:
        break

    cv2.imshow('img', img)
    cv2.waitKey(40)