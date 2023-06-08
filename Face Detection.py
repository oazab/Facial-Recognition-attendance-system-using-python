import cv2

face_cascade = cv2.Cascadeclassifier('haarcascade_fortalface_default.xml')

img = cv2.imread('test.jpg')

gray = cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectmultiscale(gray, 1.1, 4)

for (x, y, w, h) in face:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) 

cv2.imshow('img', img)
cv2.waitkey()