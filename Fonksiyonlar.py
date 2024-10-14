import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)#Çizgilerin yinelenmesini arttıran fonksiyon
print(kernel)
path="elceziri.jpg" #Uzantının değişmemesi için
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Resmi gri yapar
imgBugu = cv2.GaussianBlur(img,(5,5),5) # Buğlama yapar.
imgCanny = cv2.Canny(imgBugu,100,100) # Hatları çizer.
imgGen = cv2.dilate(imgCanny,kernel,4) # Hatları genişetme
imgDar = cv2.erode(imgGen, kernel, 1) # Hatları daraltma

cv2.imshow("original",img)
cv2.imshow("gray",imgGray)
cv2.imshow("bugulu",imgBugu)
cv2.imshow("canny",imgCanny)
cv2.imshow("genisletilmis",imgGen) # Çizgilerin kalınlığını arttırır.
cv2.imshow("daraltilmis",imgDar) # Çizgilerin kalınlığını azaltır.


#Pencere kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
