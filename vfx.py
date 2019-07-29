import cv2
import numpy as np
import matplotlib.pyplot as plt
    #USING WEB CAM
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=0
while ret:
    cv2.imshow("frame",frame)
    ret,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowcol=np.array([180,180,180])
    highcol=np.array([220,220,220])
    mask=cv2.inRange(hsv,lowcol,highcol)
    res=cv2.bitwise_and(frame,frame,mask=mask)        
    cv2.imshow("frame",res)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        #cv2.imwrite('pic.jpg',frame)
        #pc=frame
        #40,60,110    60,100,150
        break
cap.release()
cv2.destroyAllWindows()
