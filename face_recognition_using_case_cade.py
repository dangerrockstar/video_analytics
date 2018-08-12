import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('case_cade xml/haarcascade_frontalface_default.xml')

def cam(cap):
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,x),(x+w,y+h),(0,225,0),2)  
    #    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
cam(cv2.VideoCapture(0))