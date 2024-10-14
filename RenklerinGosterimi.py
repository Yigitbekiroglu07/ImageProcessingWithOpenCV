import cv2

resim = cv2.imread("camii.jpg")

print(resim.item(1,1,0)) #blue
print(resim.item(1,1,1)) #green
print(resim.item(1,1,2)) #red

cv2.imshow("cerceve",resim)
cv2.imshow("cerceve2",resim2)

#Pencere kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
