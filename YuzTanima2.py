import cv2
import numpy as np

cam = cv2.VideoCapture(0) #Kendi bilgisayarımızdan görüntü almak için

while True:
    x,cap = cam.read() #Yakalanılan görüntü okunur

    face_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #Yüz tanıma
    eye_casc = cv2.CascadeClassifier("haarcascade_eye.xml") # Göz tanıma
    smile_casc = cv2.CascadeClassifier("haarcascade_smile.xml") #Gülücük tanıma

    gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY) # Resmi gri formata çevirme

    faces = face_casc.detectMultiScale(gray,1.1,4)#resmi taratır ve büyütür
    eyes = eye_casc.detectMultiScale(gray,1.1,4)
    smiles = smile_casc.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(cap,(x,y),(x+w,y+h),(0,255,0),2) #tanımlanan resmin etrafına dikdörtgen çizilir
        cv2.putText(cap,'face',(x+w-60,y+h+17),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)#kare altına face yazar.

    for(a,b,c,d) in eyes:
        cv2.rectangle(cap,(a,b),(a+c,b+d),(255,0,0),1) #tanımlanan resmin etrafına dikdörtgen çizilir
        cv2.putText(cap,'eye',(a+c-60,b+d+17),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1) #kare altına eye yazar.

    for(k,l,m,n) in smiles:
        cv2.rectangle(cap,(k,l),(k+m,l+n),(255,0,0),1) #tanımlanan resmin etrafına dikdörtgen çizilir
        cv2.putText(cap,'smile',(k+m-60,l+n+17),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1) #kare altına smile yazar.


    cv2.imshow("goruntu",cap) # Görüntü gösterilir

    if cv2.waitKey(1) & 0xff == ord("q"):
        break


cam.release()
cv2.destroyAllWindows()
