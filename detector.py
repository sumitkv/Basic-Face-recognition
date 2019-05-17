import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('E:\Tutorial\project\haarCascade\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("E:\\Tutorial\\project\\faceReg\\recognizer\\trainingData.yml")
id = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        if id==1:
            id=""
        elif id==2:
            id=""
        elif id==3:
            id=""
        cv2.putText(img,str(id),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow('img',img)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
