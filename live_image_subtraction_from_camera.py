# import opencv module
import cv2  

cameracap=cv2.VideoCapture(0) #create Video Capture instance

fgbg = cv2.createBackgroundSubtractorMOG2() #Live video create Background Subtractor

while True:
    readval,frame=cameracap.read() #read Video Capture instance frame 
    graycolor=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #show gray Subtractor video
    hsvcolor=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #show red Subtractor video
    Subtractimage = fgbg.apply(frame) 

    # here all show frame 
    cv2.imshow('frame',frame) # live camera views here
    cv2.imshow('graycolor',graycolor) #show gray Subtractor video
    cv2.imshow('hsvcolor',hsvcolor) #show red Subtractor video
    cv2.imshow('Subtractimage',Subtractimage) 

    waitkey=cv2.waitKey(8) # fill wait key for live video 
    
cameracap.release() # release camera famre after if you kill the python script 
cv2.destroyAllWindows() # destroy all open video frame
