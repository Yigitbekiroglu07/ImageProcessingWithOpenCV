import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8) #Kare pencere oluşturma
# 0 255
print(img)

img[20:80,55:85] = 255,0,0 #kare pencerenin belirtilen yükseklik ve genişliğini maviye döndürür 
#img[:] = 255,0,0 --> tüm resmi maviye boyar
cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(0,255,0),3) #çizgi çizmek için
cv2.rectangle(img,(110,200),(450,140),(0,250,250),cv2.FILLED)#dikdörtgen çizmek için
#cv2.FILLED dikdörtgen içini doldurur. (110,200) --> başlangıç, (450,140) --> bitiş (0,250,250) --> rengi
cv2. circle(img,(150,400),75, (255,255,56),3)#daire çizmek için
# (150,400) --> başlangıç 75 = r, (255,255,56) --> renk 3 -> kalınlık
cv2.putText(img,"Yigit",(450,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,150),2)#resim üstüne yazı yazma
# (450,450) --> başlangıç noktası, cv2.FONT_HERSHEY_COMPLEX --> yazı fontu, 1--> font oranı, (0,150,150) --> rengi, 2 --> kalınlık
cv2.imshow("karaResim",img)

cv2.waitKey(0)
