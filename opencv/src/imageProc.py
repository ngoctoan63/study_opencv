'''
Created on Oct 24, 2017

@author: toannn
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
                                                    #IMREAD_GRAYSCALE: chuyen sang trang den
img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)  #IMREAD_COLOR: anh mau ko co alpha;
cv2.imshow('image',img)                             #IMREAD_UNCHANGED: giu nguyen ban
cv2.waitKey(0)
cv2.destroyAllWindows()