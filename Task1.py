"""
Jose Fernández Ortiz
"""
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

def histogram(im,num_rows, num_cols, bins):
    shape_im_row=im.shape[0]
    shape_im_col=im.shape[1]

    shape_row=shape_im_row/num_rows
    shape_col=shape_im_col/num_cols

    hist_red_conc=np.zeros((0,1))
    hist_green_conc=np.zeros((0,1))
    hist_blue_conc=np.zeros((0,1))
        
    for i in range (0,num_rows):
        for j in range (0, num_cols):
            
            mask[(i*shape_row):((i+1)*shape_row), (j*shape_col):((j+1)*shape_col)]=255
            masked_im=im.copy()
            masked_im[mask==0]=0
        
            ranges =[0,256]
            
            hist_red=cv2.calcHist([im],[2],mask,[bins],ranges)
            hist_green=cv2.calcHist([im],[1],mask,[bins],ranges)
            hist_blue=cv2.calcHist([im],[0],mask,[bins],ranges)
            hist_red_conc=np.concatenate((hist_red_conc, hist_red))
            hist_green_conc=np.concatenate((hist_green_conc, hist_green))
            hist_blue_conc=np.concatenate((hist_blue_conc, hist_blue))           
            mask[(i*shape_row):((i+1)*shape_row), (j*shape_col):((j+1)*shape_col)]=0
    
    return (hist_red_conc, hist_green_conc, hist_blue_conc) 
    

path="c:\\improc"
os.chdir(path)
im=cv2.imread('lena.jpg')

mask = np.zeros(im.shape[:2], np.uint8)

num_rows=3
num_cols=4
bins = 256
ranges = [0,num_rows*num_cols*bins]

cv2.imshow('Lena', im)

(hist_red_conc, hist_green_conc, hist_blue_conc) = histogram(im,num_rows, num_cols, bins)

plt.plot(hist_red_conc, 'r')
plt.plot(hist_green_conc, 'g')
plt.plot(hist_blue_conc, 'b')
plt.xlim(ranges)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
