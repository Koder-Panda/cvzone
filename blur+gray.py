# import cv2
# import numpy as np
#
# pic=cv2.imread("pics/Screenshot 2023-05-25 141452.png")
#
# img_colorChange=cv2.cvtColor(pic,cv2.COLOR_BGR2YCrCb)  #cvtcolor(src,cv2.WhateverColor)
# imgBlur=cv2.GaussianBlur(pic,(9,9),0)                  #GaussianBlur(src,kernelSize)
#                #size,type
# kernel=np.ones((5,5),np.uint8)                            #kerenl is a matrix . we use numpy.
# canny_edge=cv2.Canny(img_colorChange,100,100)          #Canny(src,threshold1,threshold2)
#
# dialiation=cv2.dilate(canny_edge,kernel,iterations=1)  #dialate(src,kernel,iterations i.e.,thickness)
#
# cv2.imshow("Photo",img_colorChange)
# cv2.imshow("Other",imgBlur)
# cv2.imshow("Other",canny_edge)
# cv2.imshow("Other",dialiation)
#
# cv2.waitKey(0)