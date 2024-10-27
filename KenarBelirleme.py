import cv2
import numpy as np

img=cv2.imread("satranc.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Resmi grileştirir, ama üçlü kanal formatında tutar (BGR)
img_gray=np.float32(img_gray) #resim float32 sınıfına eklenir.

koseler=cv2.goodFeaturesToTrack(img_gray,60,0.01,10) # (img_gray,resimde kaç nokta var,0.01,kaaç piksellik köşe görülecek)

koseler=np.int32(koseler)


for kose in koseler:
    x,y=kose.ravel()
    cv2.circle(img,(x,y),10,(0,255,0),-1) #köşeleri işaretlemek için kullanılır


cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
