#BattlePass
import numpy as np
import cv2
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils

from PIL import Image
import time


cap = cv2.VideoCapture('Day2.MOV')
frames_count, fps, width, height = cap.get(cv2.CAP_PROP_FRAME_COUNT), cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap2 =  cv2.VideoCapture('Day2.MOV')

width = int(width)
height = int(height)
print(cap, frames_count, fps, width, height)
  
sub = cv2.createBackgroundSubtractorMOG2()
ret, frame = cap.read()
ratio = 1.0
image = cv2.resize(frame, (0, 0), None, ratio, ratio)
#original = cv2.resize(frame, (0, 0), None, ratio, ratio)
width2, height2, channels = image.shape
num=1

path = 'Save'; data = 'image'; last = '.jpg'; test = "";
counter = 1 #Fix Coun.

while True:
    #start_time = time.time() # start time of the loop
    ret, frame = cap.read()    
    if not ret:
        frame = cv2.VideoCapture("Day2.MOV")        
        continue
    if ret: 
        image = cv2.resize(frame, (1280, 720), None, ratio, ratio)       
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fgmask = sub.apply(gray)        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel,(5, 5))
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel,(5, 5))        
        dilation2 = cv2.dilate(opening, kernel,iterations = 2)
        retvalbin, bins = cv2.threshold(dilation2 , 100, 255, cv2.THRESH_BINARY) #Disable #160
        cv2.imshow("Bins",bins)  #bins is threshold.
        
        contours, hierarchy = cv2.findContours(bins, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  #Fixed openCV 4.0
        minarea = 36000     #minarea = 500
        maxarea = 350000  #maxarea = 30000

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
                    if(cx < 1200):   #cx 1200
                        if (cy < 500): #600
                            flag = 0;                            
                        if (cx > 540) and (cx < 540 + 310):
                            x, y, w, h = cv2.boundingRect(cnt)                            
                            if (cy > 542   and (cy  < 542 + 10 )) : #Line Capture;                                 
                                    vehicle = image[y-30 : y + h+30, x-30 : x+ w]   #image from contours.
                                    #vehicle = image[320 : 320 + 370, 540 : 540 + 310]  #crop image from frame.                                  
                                    cv2.imshow('Detect', vehicle)

                                    # vehicle_Color = image[y+10 : y + h -300, x+50 : x+ w-100]                                    
                                    # cv2.imshow('Detect', vehicle)  #Config
                                    # #cv2.imshow('Detect', vehicle_Color) #K-mean

                                    # CAR = cv2.cvtColor(vehicle_Color, cv2.COLOR_BGR2RGB)
                                    # CAR = CAR.reshape((CAR.shape[0] * CAR.shape[1], 3))
                                    # clt = KMeans(n_clusters = 3)
                                    # clt.fit(CAR)

                                    # hist = utils.centroid_histogram(clt)
                                    # print("Histogram : ",hist)
                                    # bar = utils.plot_colors(hist, clt.cluster_centers_)

                                    text = ('%s%d%s' %(data, counter,last)) 
                                    if (flag==0):
                                        cv2.imwrite(os.path.join(path ,text), vehicle) #Save to Folder : Save;
                                        flag = 1;                                        
                                        counter += 1 
                            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),cv2.FONT_HERSHEY_SIMPLEX, .3,(0, 0, 255), 1)
                            cv2.drawMarker(image, (cx, cy), (0, 255, 255), cv2.MARKER_CROSS, markerSize=8,thickness=3,line_type=cv2.LINE_8)                            #print('Flag==',flag,'CX-------------------',cx,'Y----------------------',y,'Counter===',counter)
                    print("Cy " ,cy)            
                           
    cv2.rectangle(image, (540, 320), (540 + 310, 320 + 370), (0, 255, 0), 2) #cv2.rectangle(image, (840, 360), (840 + 420, 360 + 460), (0, 255, 0), 2)
    cv2.line(image,(540,542),(850,542),(0,0,255),2)  #Line                   
    cv2.imshow("Project : ", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

