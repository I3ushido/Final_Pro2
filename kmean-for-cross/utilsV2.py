import numpy as np
import cv2

def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist


def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    color = None
    color_detec = None
    c1 = 0
    c2 = 0
    c3 = 0
    # print("Max : {:.3f}".format(max(hist)))
    for (percent, color) in zip(hist, centroids):  # True
        # print("color is : ",color)
        # print("percent ", percent, "total color ", len(color), "color[0]",color[0], "color[1]", color[1], "color[2]", color[2])
        if percent > 0.4:
            c1 = int(color[0])
            c2 = int(color[1])
            c3 = int(color[2])
            # print("Color[1]:{:d} | Color[2]:{:d} | Color[3]:{:d}".format(c1,c2,c3)) #disable
            return [bar, c1, c2, c3]

        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX