import cv2
import numpy as np

frameWidth = 480 #Çerçeve Genişliği
frameHeight = 360 #Çerçeve Yüksekliği
cap=cv2.VideoCapture(0) #Bilgisayar kamerasından yapılacağı için 0 seçilir.

cap.set(3,frameWidth)
cap.set(4,frameWidth)


def empty(a):
    pass

#Tekrar oluşturma
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("Value Min","HSV",0,255,empty)
cv2.createTrackbar("Value Max","HSV",0,255,empty)

while True:
    __, img = cap.read()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max","HSV")
    s_min = cv2.getTrackbarPos("SAT Min","HSV")
    s_max = cv2.getTrackbarPos("SAT Max","HSV")
    v_min = cv2.getTrackbarPos("Value Min","HSV")
    v_max = cv2.getTrackbarPos("Value Max","HSV")
    # print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img,mask,result])

    #cv2.imshow("original",img)
    #cv2.imshow("HSV image",imgHsv)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("result",result)
    cv2.imshow("genel",hstack)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
#Pencere kapatma  
cap.release()
cv2.destroyAllWindows()
