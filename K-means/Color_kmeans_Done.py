from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utilsV2
import cv2
import numpy as np
import sys
import collections
import webcolors
# np.set_printoptions(threshold=sys.maxsize) #FullPrint
#17 sep
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

kGroup = 2

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
image = cv2.imread("nike.png") #R: R: 27.243 	 G: 131.513 	 B: 62.893

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
hist = utilsV2.centroid_histogram(clt)#Com
print("Histogram :  ",hist)#Com
bar = utilsV2.plot_colors(hist, clt.cluster_centers_)#Com
# bar2 = utils.plot_colors(clt.labels_, clt.cluster_centers_)

print("c1 : {:d}".format(bar[2]))
requested_colour = (bar[2], bar[3], bar[4])
actual_name, closest_name = get_colour_name(requested_colour)
print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)


plt.figure()
plt.axis("off")
plt.imshow(bar[0])
plt.show()

