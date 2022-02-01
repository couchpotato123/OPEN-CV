import cv2

faceCascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_russian_plate_number.xml')

img = cv2.imread('car1.jpg')

faces = faceCascade.detectMultiScale(img,scaleFactor=1.2,minNeighbors = 5, minSize=(25,25))

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('plate',img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()