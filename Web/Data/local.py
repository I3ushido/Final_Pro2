from flask import Flask, jsonify, request
import pymysql
import os
import base64
import requests as rep
from PIL import Image
from io import BytesIO
import json

# C:\Users\Renka\Desktop\flask\flask

app = Flask(__name__)
# conn = pymysql.connect('localhost', 'root', '', 'car_db')
conn = pymysql.connect('localhost', 'cars99', 'admin99', 'car_detection')
last_id = ''

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you send' : some_json['name']}), 201
    else:
        return jsonify({"name": "Dark"})

@app.route('/add/<int:num>', methods=['GET'])
def add(num):
    return jsonify({'result' : num + 100})

@app.route('/inserts', methods=['POST'])
def insert_data():
    global last_id
    if request.method == 'POST':
        data_json = request.get_json()
        with conn:
            video_time = data_json['video_time']
            cur = conn.cursor()
            sql = "INSERT INTO video (video_time) VALUES (%s)"
            val = [(video_time)]
            # val = [(video_time)]
            cur.executemany(sql, val)
            conn.commit()
            print(cur.rowcount, "record was inserted")
            last_id = cur.lastrowid
            print(last_id)
            return jsonify(), 200

@app.route('/inserts_data', methods=['POST'])
def insert_datas():
    global last_id
    if request.method == 'POST':
        data_json = request.get_json()
        with conn:

            speed = data_json['speed']
            car_colors = data_json['car_colors']
            car_category = data_json['car_category']
            car_brand = data_json['car_brand']
            # car_time = data_json['car_time']
            car_image = data_json['car_image']
            cur = conn.cursor()
            sql = "INSERT INTO car (speed, car_colors, car_category, car_brand, car_image, car_vid) VALUES (%s ,%s, %s, %s, %s, %s)"
            val = [(speed, car_colors, car_category, car_brand, car_image, int(last_id))]
            cur.executemany(sql, val)
            conn.commit()
            print(cur.rowcount, "record was inserted")
            return jsonify(), 200

@app.route('/moon/<string:data>', methods=['GET'])
def moon(data):
    return jsonify({'data' : data})

@app.route('/img', methods=['POST'])
def images():
    image64 = request.get_json()
    data = image64['image']
    name = image64['name']
    im = Image.open(BytesIO(base64.b64decode(data)))
    # im.save('img//accept.png', 'PNG')
    im.save('img//'+name, 'PNG')
    return jsonify({'data' : image64}), 200

if __name__ == '__main__':
    # app.run(host='206.189.46.191',port=443,debug=True)
    # app.run(debug=True)
    app.run(host='206.189.46.191',port=443,debug=True)
