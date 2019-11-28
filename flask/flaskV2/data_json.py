import requests as reqs
from flask import Flask, jsonify, request
import requests as rep
import json
# C:\Users\Renka\Desktop\flask\flask
print("--------------------------------------------------------------")
data = {"project_speed"  : "Unknou","project_colors" : "white","project_category" : "SUV","project_brand" : "toyota","project_image"  : "./img/2.png"}
# app_data = json.dumps(data)
print(data)
response = reqs.post('http://206.189.46.191:443/inserts',json=data)
print(response.text), 200
