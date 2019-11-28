import base64
import requests as rep
from PIL import Image
from io import BytesIO
import json

with open("nike.png","rb") as file:
    data = base64.b64encode(file.read())
    print(type(data))
    #print(base64.b64encode(file.read()))
    print(data)
    file = open("test.txt","wb")
    file.write(data)
    file.close()
    #encoding = 'utf-8'
    #data.decode(encoding)
    #data2 = str(data2)
    data = data.decode('utf8')
    data2 = "data:image/jpeg;base64,/"+data
    print(data2)
    print("data : ",data2)
    #payload = json.dumps({'image' : data2})
    #print(payload)
payload = {'image' : data2}
#payload = json.dumps(payload)
r = rep.post("http://206.189.46.191/car/receive.php", json=payload)
#print(r.text)

#Convert text to image.
##f = open('test.txt', 'r')
##data = f.read()
##f.closed
##im = Image.open(BytesIO(base64.b64decode(data)))
##im.save('image64N.png', 'PNG')

###Convert from variable
##data = b'''iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAIBJRE
##          FUOMvN08ENgCAMheG/TGniEo7iEiZuqTeiUkoLHORK++Ul8ODPZ92XS2ZiADITmwI+sWHwi
##          w2BGtYN1jCAZF1GMYDkGfJix3ZK8g57sJywteTFClBbjmAq+ESiGIBEX9nCqgl7sfyxIykt
##          7NUUD9rCiupZqAdTu6yhXgzgBtNFSXQ1+FPTAAAAAElFTkSuQmCC'''
##im = Image.open(BytesIO(base64.b64decode(data)))
##im.save('accept.png', 'PNG')
