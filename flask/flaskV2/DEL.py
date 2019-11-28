import os
import  cv2
import base64
import requests as reqs
from io import BytesIO
from PIL import Image
import pyperclip
## format
# a = '{:01.4f}'.format(3.141592653589793)
# print('data : ',a)


## delete ioimage
# try:
#     os.remove("777.png")
# except: pass


#image64RB
filename = '272.jpg'
im=Image.open(filename)
with open(filename, "rb") as img:
  imgbase = str(base64.b64encode(img.read()))
x = imgbase.split("'")
str = x[1]
pyperclip.copy(str)
spam = pyperclip.paste()
print('data: ', str)
data = {'logo': str}
response = reqs.post('http://127.0.0.1:5000/logo',json=data)
print('call back : ', response.text)
