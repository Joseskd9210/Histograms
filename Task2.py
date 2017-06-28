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
im=cv2.imread('im1.jpg', cv2.IMREAD_GRAYSCALE)
im2=cv2.equalizeHist(im)
im3=cv2.imread('im2.jpg')
im3=cv2.resize(im3, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

im_yuv = cv2.cvtColor(im3, cv2.COLOR_BGR2YUV)

im_yuv[:,:,0]=cv2.equalizeHist(im_yuv[:,:,0])

im4=cv2.cvtColor(im_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Original Grayscale image',im)
cv2.imshow('Equilized Grayscale image',im2)

cv2.imshow('Original color image',im3)
cv2.imshow('Equilized color image',im4)

cv2.waitKey()
cv2.destroyAllWindows()