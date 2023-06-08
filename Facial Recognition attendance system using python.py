import cv2

face_cascade = cv2.Cascadeclassifier('haarcascade_fortalface_default.xml')

cap = cv2.videocapture(0)

while True:

_, img = cap.read()

gray = cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectmultiscale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) 


cv2.imshow('img', img)

k = cv2.waitkey(30) & 0xff
if k==27:
    break


cv2.release()