import cv2
import numpy as np
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
import os,shutil
import os


Folder = 4


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def createFolder_Dataset(directory,TotalFolder):
    # print('directory : ' + directory + ' TotalFolder : ' + TotalFolder)
    i = 1
    while i <= TotalFolder:
        try:
            if not os.path.exists(directory):                
                os.makedirs(directory+str(i))
                print(directory+str(i))
        except OSError:
            print ('Error: Creating directory. ' +  directory)
        i+=1

    print(TotalFolder)


##createFolder_Dataset('Pre_Dataset/Out',Folder)
createFolder_Dataset('./Out',Folder)

countn = 1
while countn <= Folder:
    count=str(countn)
    mypath=''+count
    #mypath='In'+count
    outpath='Out'+count+'/'
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    for n in range(0, len(onlyfiles)):
        # To convert single page
        path2=''+onlyfiles[n]
        path4=mypath+'/'+path2+''
        #print(path4)
        images = cv2.imread(path4)
        width = 350
        height = 450
        dim = (width, height)
        # resize imag
        images = cv2.resize(images, dim, interpolation = cv2.INTER_AREA)
        img_tmp = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
        _ ,img_gray = cv2.threshold(img_tmp,220,255,cv2.THRESH_BINARY)
        #crop_img = img_gray[0:375, 0:1300]
        cv2.imwrite(outpath+'/'+onlyfiles[n],img_gray)
        countn = int(count)+ 1  # This is the same as count = count + 1
        print(onlyfiles[n])
print('sucess')
