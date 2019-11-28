from PIL import Image
import glob
import base64
import requests as reqs
from io import BytesIO

image_list = []
for filename in glob.glob('data2/*.png'):
    im=Image.open(filename)
    # image_list.append(im)
    with open(filename, "rb") as img:
      imgbase = str(base64.b64encode(img.read()))
    x = imgbase.split("'")

    # stringpic = 'data:image/jpg;base64,' + x[1]
    stringpic = x[1]
    filename = filename.split("data2\\")
    print("FileName : ", filename[1])
    # print("base64 : ", stringpic)
    print("--------------------------------------------------------------")
    data = {'image': stringpic,'name' : filename[1]}
    response = reqs.post('http://206.189.46.191:443/img',json=data)
    # response = reqs.post('http://127.0.0.1:5000/img',json=data)
    # print(response.text)
