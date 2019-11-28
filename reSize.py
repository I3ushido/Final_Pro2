import os
from scipy import ndimage, misc

images = []
for root, dirnames, filenames in os.walk("/foo/bar"):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            filepath = os.path.join(root, filename)
            image = ndimage.imread(filepath, mode="RGB")
            image_resized = misc.imresize(image, (64, 64))
            images.append(image_resized)