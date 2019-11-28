import base64
import requests as rep
from PIL import Image
from io import BytesIO
import json

#Convert text to image.
##f = open('test.txt', 'r')
##data = f.read()
##f.closed
##im = Image.open(BytesIO(base64.b64decode(data)))
##im.save('image64N.png', 'PNG')

#Convert from variable
data = b'''iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAIBJRE
          FUOMvN08ENgCAMheG/TGniEo7iEiZuqTeiUkoLHORK++Ul8ODPZ92XS2ZiADITmwI+sWHwi
          w2BGtYN1jCAZF1GMYDkGfJix3ZK8g57sJywteTFClBbjmAq+ESiGIBEX9nCqgl7sfyxIykt
          7NUUD9rCiupZqAdTu6yhXgzgBtNFSXQ1+FPTAAAAAElFTkSuQmCC'''


im = Image.open(BytesIO(base64.b64decode(data)))
im.save('accept.png', 'PNG')
