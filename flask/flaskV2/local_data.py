import requests as reqs
from flask import Flask, jsonify, request
import requests as rep
import json
import re
# C:\Users\Renka\Desktop\flask\flask
def data1():
    info = {"video_time" : "mornimg"}
    response = reqs.post('http://127.0.0.1:5000/inserts',json=info)
    print(response.text), 200

def data2():
    count = 1
    f = open("output.txt", "r")
    for x in f:
        # print(x)
        datas = x.split(" ")
        datas3 = datas[3].split("\n")
        print(datas[0], datas[1], datas[2], datas3[0], '/img/car_' + str(count) + '.png')
        data = {"car_category"  : datas[0],"car_colors" : datas[1],"car_brand" : datas[2],"speed" : datas3[0],"car_image"  : '/img/car_' + str(count) + '.png'}
        # app_data = json.dumps(data)
        print(data)
        response = reqs.post('http://127.0.0.1:5000/inserts_data',json=data)
        print(response.text), 200
        count += 1


data2()




# data = {"project_speed"  : "Unknou","project_colors" : "white","project_category" : "SUV","project_brand" : "toyota","project_image"  : "./img/2.png"}
# # app_data = json.dumps(data)
# print(data)
# response = reqs.post('http://127.0.0.1:5000/inserts_data',json=data)
# print(response.text), 200
