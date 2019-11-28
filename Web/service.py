from flask import Flask, jsonify, request, render_template, url_for,redirect
import pymysql
import os
from PIL import Image
import glob
import base64
import requests as reqs
from io import BytesIO

app = Flask(__name__)
conn = pymysql.connect('localhost', 'cars99', 'admin99', 'car_detection')

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you send' : some_json['name']}), 201
    else:
        return jsonify({"name": "Dark"})

@app.route('/add/<int:num>',methods=['GET'])
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
            sql = "INSERT INTO project2 (project_speed, project_colors, project_category, project_brand, project_image) VALUES (%s ,%s ,%s, %s, %s)"
            val = [(speed, color, category, brand, path)]
            cur.executemany(sql, val)
            conn.commit()
            print(cur.rowcount, "record was inserted")
            # return render_template('insert.html')
            return jsonify(data_json), 200


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
    im.save('cross/img//'+name, 'PNG')
    return jsonify({'data' : image64}), 201



@app.route('/del', methods=['GET'])
def delete_():
    with conn:
        cursor= conn.cursor()
        cursor.execute("TRUNCATE TABLE project2")
        return jsonify({'info' : 'Drop table complete.'})

if __name__ == '__main__':
    app.run(host='206.189.46.191',port=443,debug=True)
