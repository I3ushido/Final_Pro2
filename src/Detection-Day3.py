#BattlePass
import numpy as np
import cv2
import os

import time

cap = cv2.VideoCapture('Day3/D3-1.MOV')
frames_count, fps, width, height = cap.get(cv2.CAP_PROP_FRAME_COUNT), cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap2 =  cv2.VideoCapture('Day3/D3-1.MOV')

width = int(width)
height = int(height)
print(cap, frames_count, fps, width, height)
  
sub = cv2.createBackgroundSubtractorMOG2()
ret, frame = cap.read()
ratio = 1
image = cv2.resize(frame, (0, 0), None, ratio, ratio)
#original = cv2.resize(frame, (0, 0), None, ratio, ratio)
width2, height2, channels = image.shape
num=1

path = 'Save'; data = 'image'; last = '.jpg'; test = "";
counter = 1 #Fix Coun.

while True:
    ret, frame = cap.read()    
    if not ret:
        frame = cv2.VideoCapture("Day3/D3-1.MOV")        
        continue
    if ret: 
        image = cv2.resize(frame, (1280, 720), None, ratio, ratio)       
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fgmask = sub.apply(gray)        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)        
        dilation2 = cv2.dilate(opening, kernel,iterations = 2)
        retvalbin, bins = cv2.threshold(dilation2 , 160, 255, cv2.THRESH_BINARY) #Disable 
        #cv2.imshow("Bins",bins)  #bins is threshold. #Disable
        
        contours, hierarchy = cv2.findContours(bins, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  #Fixed openCV 4.0
        minarea = 36000     #minarea = 500
        maxarea = 350000    #maxarea = 30000

        cxx = np.zeros(len(contours))
        cyy = np.zeros(len(contours))        
        
        for i in range(len(contours)):           
            if hierarchy[0, i, 3] == -1:
                area = cv2.contourArea(contours[i])                
                if minarea < area < maxarea:              
                    cnt = contours[i]
                    M = cv2.moments(cnt)
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])                                        
                    if(cx >= 500 and cx <= 950):   #cx 1200
                        if (cy < 400): #600
                            flag = 0;                            
                        #if (cx > 540) and (cx < 540 + 310):
                        if (cx >= 500) and (cx <= 875):
                            x, y, w, h = cv2.boundingRect(cnt)                            
                            if (cy > 470   and (cy  < 470 + 30 )): #Line Capture;                                 
                                    vehicle = image[y-30 : y + h+30, x-30 : x+ w]                                    
                                    cv2.imshow('Detect', vehicle)  #Config                                                                       
                                    text = ('%s%d%s' %(data, counter,last)) 
                                    if (flag==0):
                                        cv2.imwrite(os.path.join(path ,text), vehicle) #Save to Folder : Save;
                                        flag = 1;                                        
                                        counter += 1 
                            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),cv2.FONT_HERSHEY_SIMPLEX, .3,(0, 0, 255), 1)
                            cv2.drawMarker(image, (cx, cy), (0, 255, 255), cv2.MARKER_CROSS, markerSize=8,thickness=3,line_type=cv2.LINE_8)                            #print('Flag==',flag,'CX-------------------',cx,'Y----------------------',y,'Counter===',counter)
                    print('CX : ',cx,' CY : ',cy)        
        #print("sum_pix : ", sum_pix)                     
    image = cv2.rectangle(image, (540, 320), (540 + 310, 320 + 370), (0, 255, 0), 2) #cv2.rectangle(image, (840, 360), (840 + 420, 360 + 460), (0, 255, 0), 2)
    image = cv2.rectangle(image, (500, 212), (875, 690), (255, 0, 0), 2) #xy มุมบนซ้าย xyล่างขวา
    image = cv2.line(image,(540,542),(850,542),(0,0,255),2)  #Line
    image = cv2.line(image,(500,470),(875,470),(0,140,255),2)  #Line  Orenge       BGR RGB          
    image = cv2.imshow("Day3 : Pro1",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

