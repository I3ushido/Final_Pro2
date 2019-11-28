from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2

image = cv2.imread("car.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.figure()
plt.axis("off")
plt.imshow(image)

image = image.reshape((image.shape[0] * image.shape[1], 3))
clt = KMeans(n_clusters = 2)
clt.fit(image)

hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
