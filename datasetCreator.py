import cv2
import numpy as np
#import sqlite3

face_cascade = cv2.CascadeClassifier('E:\Tutorial\project\haarCascade\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
"""
def insertOrUpdate(Id,Name):
    connect=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=connect.execute(cmd)
    isRecordExist=0
    for row in cursor :
        isRecordExist=1
    if isRecordExist==1:
        cmd="UPDATE People SET Name="+str(Name)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name) Values("+str(Id)+","+str(Name)+")"
    connect.execute(cmd)
    connect.comit()
    connect.close()
"""
        
id=input("Enter user id: ")
#name=input("Enter your Name: ")

#insertOrUpdate(id,name)
sampleNum=0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100)

    cv2.imshow('face',img)
    cv2.waitKey(1)
    if sampleNum > 30:
        break


cam.release()
cv2.destroyAllWindows()
