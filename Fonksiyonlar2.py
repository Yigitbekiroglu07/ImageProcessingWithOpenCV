import cv2

path = "bogaz.jpg"


img = cv2.imread(path)
print(img.shape) #resim boyutu öğrenme

width, height = 400,400
imgRes = cv2.resize(img,(width,height)) #Pencere boyutunu ayarlama (burada küçülttük)
print(imgRes.shape) #resim boyutu öğrenme
imgCrop = img[50:340,200:450] #kenarları atmak için, resmi kesmeye yarar.
imgCropRes = cv2.resize(imgCrop,(img.shape[1],img.shape[0])) #resmi orijinal boyutu haline getirme

cv2.imshow("normal",img)
cv2.imshow("resize",imgRes)
cv2.imshow("cropped",imgCrop)
cv2.imshow("CropRes",imgCropRes)

#Pencere kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
