import numpy as np
import cv2

import webcolors

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
################################################################################
def centroid_histogram(clt):	
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)	
	hist = hist.astype("float") 
	hist /= hist.sum()
	return hist
def plot_colors(hist, centroids):	
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0
	color = None
	color_detec = None
	print("Max : {:.3f}".format(max(hist)))	
	for (percent, color) in zip(hist, centroids):		#True
		#print("color is : ",color)					
		#print("percent ", percent, "total color ", len(color), "color[0]",color[0], "color[1]", color[1], "color[2]", color[2])
		if percent > 0.4:
                    print("Hi")
			
		# print("percent : {:.3f} ".format(percent))
		print("R: {:.3f} \t G: {:.3f} \t B: {:.3f}".format(color[0], color[1], color[2]))
		# print("R: ",color[0]," G: ",color[1], " B: ",color[2])
		endX = startX + (percent * 300)
				
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),color.astype("uint8").tolist(), -1)		
		startX = endX
		color = color_detec

	return [bar , color]   





#original code
##def plot_colors(hist, centroids):	
##	bar = np.zeros((50, 300, 3), dtype = "uint8")
##	startX = 0
##	color = None
##	color_detec = None
##	print("Max : {:.3f}".format(max(hist)))	
##	for (percent, color) in zip(hist, centroids):		#True
##		#print("color is : ",color)					
##		#print("percent ", percent, "total color ", len(color), "color[0]",color[0], "color[1]", color[1], "color[2]", color[2])
##		if percent > 0.4 and color[0] >= 230 and color[1] >= 230 and color[2] >= 170:  #Gold
##			# print("#Gold Color ")
##			color_detec = '#Gold'
##		elif percent > 0.4 and color[0] >= 200 and color[1] >= 200 and color[2] >= 200:  #White
##			# print("#White Color ")
##			color_detec = '#White'
##		elif percent > 0.4 and color[0] >= 200 and color[1] >= 170 and color[2] >= 80: #Yellow
##			# print("#Yellow Color ")
##			color_detec = '#Yellow'
##		elif percent > 0.4 and color[0] >= 160 and color[1] >= 180 and color[2] >= 180: #Silver
##			# print("#Silver Color ")
##			color_detec = '#Sliver'			
##		elif percent > 0.4 and color[0] >= 140 and color[1] >= 50 and color[2] >= 60: #Red
##			# print("#Red Color ")
##			color_detec = '#Red'
##		elif percent > 0.4 and color[0] >= 150 and color[1] >= 100 and color[2] >= 100: #Orenge
##			# print("#Orenge Color ")
##			color_detec = '#Orenge'
##		elif percent > 0.4 and color[0] >= 90 and color[1] >= 110 and color[2] >= 150: #Blue
##			# print("#Blue Color ")
##			color_detec = '#Blue'
##		elif percent > 0.4 and color[0] >= 10 and color[1] >= 100 and color[2] >= 10: #Blue
##		# print("#Blue Color ")
##			color_detec = '#Green'
####		elif percent > 0.4 and color[0]  >= 1 and color[1] >= 1 and color[2] >= 1: #Black
####			print("#Black Color ")
##		# print("percent : {:.3f} ".format(percent))
##		print("R: {:.3f} \t G: {:.3f} \t B: {:.3f}".format(color[0], color[1], color[2]))
##		# print("R: ",color[0]," G: ",color[1], " B: ",color[2])
##		endX = startX + (percent * 300)
##				
##		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),color.astype("uint8").tolist(), -1)		
##		startX = endX
##		color = color_detec
##
##	return [bar , color]   #https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/

