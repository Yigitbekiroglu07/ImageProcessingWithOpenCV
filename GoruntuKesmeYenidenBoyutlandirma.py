import cv2
import numpy as np

# Resimleri oku
img1 = cv2.imread("man.jpg", 0)
img2 = cv2.imread("woman.jpg")

# Boyutları kontrol et
print(img1.shape)
print(img2.shape)

# Resimleri yeniden boyutlandır
img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  # img2'yi img1'e göre boyutlandır

# img1'i 3 kanallı hale getir
img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

# Yatay ve dikey birleştirme
yatay = np.hstack((img1, img2))
dikey = np.vstack((img1, img2))

# Pencereleri göster
cv2.imshow('Dikey', dikey)
cv2.imshow('Yatay', yatay)

# Pencereyi kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()


