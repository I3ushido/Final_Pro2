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
    if request.method == 'POST':
        data_json = request.get_json()
        with conn:
            speed = data_json['project_speed']
            color = data_json['project_colors']
            category = data_json['project_category']
            brand = data_json['project_brand']
            path = data_json['project_image']

            cur = conn.cursor()
            sql = "INSERT INTO projectcar (speed, color, category, brand, path) VALUES (%s ,%s ,%s, %s, %s)"
            val = [(speed, color, category, brand, path)]
            cur.executemany(sql, val)
            conn.commit()
            print(cur.rowcount, "record was inserted")
            # return render_template('insert.html')
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
