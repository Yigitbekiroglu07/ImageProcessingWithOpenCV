import cv2
import numpy as np

cv2.namedWindow("resim", cv2.WINDOW_NORMAL) #Pencere boyut ayarlama
def mousePoints(event,x,y,flags,params): # Tıklanıldığında noktayı belirleyecek fonk.
    if event == cv2.EVENT_LBUTTONDOWN: #Sol tık yapıldığında anlayacak fonk.
        print(x,y)



        
img = cv2.imread("kitap.jpg")
cv2.imshow("resim", img)
cv2.setMouseCallback("resim",mousePoints)#Pencere boyut okuma - Okunan resim çerçevesi


cv2.waitKey(0)
