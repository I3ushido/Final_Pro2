import base64
import requests as reqs

with open('mo.jpg', "rb") as img:
  imgbase = str(base64.b64encode(img.read()))
x = imgbase.split("'")

stringpic = 'data:image/jpg;base64,' + x[1]
data = {'image': stringpic}
response = reqs.post('http://206.189.46.191/car/receive.php', json=data)
print(response.text)



