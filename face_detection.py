import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpeg')
img2 = cv2.imread('test2.jpg')
img3 = cv2.imread('test3.jpg')
img4 = cv2.imread('test4.jpg')
img5 = cv2.imread('test5.jpg')
img6 = cv2.imread('t1.jpg')
img7 = cv2.imread('t2.jpg')
img8 = cv2.imread('t3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
gray5 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
gray6 = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
gray7 = cv2.cvtColor(img7, cv2.COLOR_BGR2GRAY)
gray8 = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 10)
faces2 = face_cascade.detectMultiScale(gray2, 1.1, 4)
faces3 = face_cascade.detectMultiScale(gray3, 1.1, 9)
faces4 = face_cascade.detectMultiScale(gray4, 1.1, 4)
faces5 = face_cascade.detectMultiScale(gray5, 1.1, 4)
faces6 = face_cascade.detectMultiScale(gray6, 1.1, 10)
faces7 = face_cascade.detectMultiScale(gray7, 1.1, 4)
faces8 = face_cascade.detectMultiScale(gray8, 1.1, 7)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces3:
    cv2.rectangle(img3, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces4:
    cv2.rectangle(img4, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces5:
    cv2.rectangle(img5, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces6:
    cv2.rectangle(img6, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces7:
    cv2.rectangle(img7, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces8:
    cv2.rectangle(img8, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('image1', img)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)
cv2.imshow('image4', img4)
cv2.imshow('image5', img5)
cv2.imshow('image6', img6)
cv2.imshow('image7', img7)
cv2.imshow('image8', img8)
cv2.waitKey()
