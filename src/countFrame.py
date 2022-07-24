import numpy as np
import cv2
import time

cap = cv2.VideoCapture('Day2.MOV')




start_time = time.time() 
x = 1 # displays the frame rate every 1 second
counter = 0

while(cap.isOpened()):

    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)

    counter+=1
    if (time.time() - start_time) > x :
        print("FPS: ", counter / (int)(time.time() - start_time))
        counter = 0
        start_time = time.time()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    
 






