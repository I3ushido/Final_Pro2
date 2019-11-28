from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2

import numpy as np
import sys
import collections
# np.set_printoptions(threshold=sys.maxsize) #FullPrint

kGroup = 2
image = cv2.imread("car_2.jpg")
##image = cv2.imread("Save//day3-5_1.jpg") #Gold
# image = cv2.imread("Red.jpg") #Gold
#image = cv2.imread("GoldBar.jpg") #Gold
# image = cv2.imread("BarSilverCar.jpg") #Silver
#image = cv2.imread("car.jpg") #whitecar
#image = cv2.imread("BarSilverCar.jpg") #Silver
# image = cv2.imread("BlueCar.jpg") #R: 90.820 	 G: 115.035 	 B: 165.708
# image = cv2.imread("BarOrengeCar.jpg")
# image = cv2.imread("yellowC.jpg")
# image = cv2.imread("yel.jpg") #R:  237.37837507636124  G:  198.43762981062716  B:  91.61624923640849
# image = cv2.imread("BlackCar.jpg") #black
##image = cv2.imread("green.png") #R: R: 27.243 	 G: 131.513 	 B: 62.893

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#hsv_val = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
#print("hsv_val : ",hsv_val)

plt.figure()
plt.axis("off")
plt.imshow(image)
image = image.reshape((image.shape[0] * image.shape[1], 3))
clt = KMeans(n_clusters = kGroup)
clt.fit(image)

print("cluster_centers_",clt.cluster_centers_)
# myarray = np.array(clt.labels_)
# print("labels_ ",myarray )
# CC = collections.Counter(myarray)
# CT = min(myarray),max(myarray)
# print("Counter Max : ",max(CT))
# plt.scatter(image[:,0],image[:,1], c=clt.labels_, cmap='rainbow')
# result = zip(clt.cluster_centers_, CT)
# print("list : ",list(result))
# for ch in zip(clt.cluster_centers_, CT):
#     print(ch)
##plt.imshow(image)
hist = utils.centroid_histogram(clt)#Com
print("Histogram :  ",hist)#Com
bar = utils.plot_colors(hist, clt.cluster_centers_)#Com
# bar2 = utils.plot_colors(clt.labels_, clt.cluster_centers_)
# print("bar2 : ",bar2)
print("Color : ",bar[1])
plt.figure()
plt.axis("off")
plt.imshow(bar[0])
plt.show()

