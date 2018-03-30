# -*- coding:utf-8 -*-
import sys
sys.path.append('d:/anaconda2/lib/site-packages')
#d:/anaconda2/lib/site-packages
import numpy as np
import cv2

catPath = "C:/Users/Administrator/Desktop/Aran-master/haarcascade_frontalcatface.xml"
cat_Cascade = cv2.CascadeClassifier(catPath)

def detectCat(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cat_Cascade.detectMultiScale(
    gray,
    scaleFactor= 1.11121,
    minNeighbors=16,
    minSize=(150, 150),
    flags=cv2.CASCADE_SCALE_IMAGE
    )   

    catCount = 0
    for (x, y, w, h) in faces:
        catCount += 1
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(img,'Cat',(x,y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imwrite('assets/cat.jpg', img)
    cv2.destroyAllWindows()
    return catCount