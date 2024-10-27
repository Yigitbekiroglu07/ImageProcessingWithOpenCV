import cv2
import numpy as np

img = cv2.imread("barkod.jpg")

laplacian = cv2.Laplacian(img, cv2.CV_64F) # yatay çizgiler atar

sobel= cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) # dikey çizgiler atar

cv2.imshow("orijinal",img)
cv2.imshow("laplacian",laplacian)
cv2.imshow("sobel",sobel)
