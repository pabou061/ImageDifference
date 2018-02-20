import numpy as np
import cv2

#reading all images
#img1 = cv2.imread('images/img02_0076.bmp',0)
#img2 = cv2.imread('images/img02_0077.bmp',0)

#img1 = cv2.imread('images/img02_0077.bmp',0)
#img2 = cv2.imread('images/img02_0078.bmp',0)


#img1 = cv2.imread('images/park466.bmp',0)
#img2 = cv2.imread('images/park467.bmp',0)

img1 = cv2.imread('images/park467.bmp',0)
img2 = cv2.imread('images/park468.bmp',0)

#creating a window
cv2.namedWindow('image1')

#method called when creating a trackbar
def on_trackbar(number):
    _ ,thresh = cv2.threshold(diff, number, 255, cv2.THRESH_BINARY)
    cv2.imshow('image1', thresh)	
    cv2.waitKey(0)

#pixel difference
diff = cv2.subtract(img1,img2)

#create a trackbar
cv2.createTrackbar('trackbar', 'image1', 0 , 255, on_trackbar)

#initialize
on_trackbar(0)



