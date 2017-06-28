# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

path="c:\\improc"
os.chdir(path)

im=cv2.imread('lena.jpg')
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
im=cv2.resize(im, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
im_yuv = cv2.cvtColor(im, cv2.COLOR_BGR2YUV)
im_yuv[:,:,0]=clahe.apply(im_yuv[:,:,0])
im2=cv2.cvtColor(im_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Original',im)
cv2.imshow('Yuv',im2)

cv2.waitKey()
cv2.destroyAllWindows()