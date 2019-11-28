import numpy as np
import cv2



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
	c1 = 0
	c2 = 0
	c3 = 0
	print("Max : {:.3f}".format(max(hist)))	
	for (percent, color) in zip(hist, centroids):		#True
		#print("color is : ",color)					
		#print("percent ", percent, "total color ", len(color), "color[0]",color[0], "color[1]", color[1], "color[2]", color[2])
		if percent > 0.4:
                    c1 = int(color[0])
                    c2 = int(color[1])
                    c3 = int(color[2])
                    print("c1 {:d} ; c2 {:d} ; c3 {:d}".format(c1,c2,c3))		
		#print("R: {:.3f} \t G: {:.3f} \t B: {:.3f}".format(color[0], color[1], color[2]))
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),color.astype("uint8").tolist(), -1)		
		startX = endX
		color = color_detec
		#print("c1 {:d} ; c2 {:d} ; c3 {:d}".format(c1,c2,c3))
	return [bar , color ,c1 ,c2, c3]

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


