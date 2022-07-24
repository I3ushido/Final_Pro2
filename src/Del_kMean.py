import numpy as np
import cv2

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils



# img = cv2.imread('white.jpg')
# img = cv2.imread('image128.jpg')
# img = cv2.imread("GoldBar.jpg") #Gold
# img = cv2.imread("BarSilverCar.jpg") #Silver
#image = cv2.imread("car.jpg") #whitecar
#image = cv2.imread("BarSilverCar.jpg") #Silver
#image = cv2.imread("BlueCar.jpg")
# img = cv2.imread("BarOrengeCar.jpg")
# img= cv2.imread("BlackCar.jpg") #black
img= cv2.imread("day3-5_1.jpg") #black

Z = img.reshape((-1,3))
#convert
Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
clt = ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
print('Color : ', center)

#convert back
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure()
plt.axis("off")
# plt.imshow(image)

image = res2
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.reshape((image.shape[0] * image.shape[1], 3))
clt = KMeans(n_clusters = 2)
clt.fit(image)

plt.imshow(image)
hist = utils.centroid_histogram(clt)
print("Histogram : ",hist, "\n")
bar = utils.plot_colors(hist, clt.cluster_centers_)

plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()


