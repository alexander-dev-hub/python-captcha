# draw histogram in python. 
import cv2
import numpy as np
 
print(cv2.__version__)



image = cv2.imread('test/sci-hub1.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", image)
cv2.imshow("Over the Clouds - gray", gray_image)
#cv2.waitKey(0)



h = np.zeros((300,256,3))
 
bins = np.arange(256).reshape(256,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]
 
for ch, col in enumerate(color):
    hist_item = cv2.calcHist([image],[ch],None,[256],[0,255])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)
 
h=np.flipud(h)
 
cv2.imshow('colorhist',h)
cv2.waitKey(0)