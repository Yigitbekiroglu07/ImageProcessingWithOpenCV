import cv2

# Video dosyasını okuma
video = cv2.VideoCapture("1.mp4")

# Doğru bir şekilde açılıp açılmadığını kontrol edin
if not video.isOpened():
    print("Video dosyası açılamadı.")
else:
    while True:
        ret, img = video.read()
        if not ret:
            print("Görüntü alınamadı veya video sona erdi.")
            break
        
        # Görüntüyü gösterme
        cv2.imshow("video1", img)
        
        # Çıkmak için 'q' tuşuna basma kontrolü
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Pencereleri kapatma
video.release()
cv2.destroyAllWindows()
