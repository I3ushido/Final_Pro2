from flask import Flask, jsonify, request
import pymysql
import os
import base64
import requests as rep
from PIL import Image
from io import BytesIO
import json
import sys
import cv2
from decimal import Decimal
import numpy as np
import pandas as pd
from scipy.misc import imread, imresize
from sklearn.metrics import accuracy_score
import tensorflow as tf
from PIL import Image
from sklearn.metrics import confusion_matrix
import pylab as pl
from sklearn.metrics import precision_recall_fscore_support as score

import tflearn
from sklearn.model_selection import train_test_split
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

nclass_logos = 10
model_logos = None

app = Flask(__name__)


@app.route('/', methods=['GET'])
def load_model():
    global nclass_logos
    global model_logos
    networks = input_data(shape=[None, 128, 128, 3], name='input')
    networks = conv_2d(networks, 32, 3, activation='relu', regularizer="L2")
    networks = max_pool_2d(networks, 2)

    networks = local_response_normalization(networks)
    networks = conv_2d(networks, 64, 3, activation='relu', regularizer="L2")
    networks = max_pool_2d(networks, 2)

    networks = local_response_normalization(networks)
    networks = conv_2d(networks, 128, 3, activation='relu', regularizer="L2")
    networks = max_pool_2d(networks, 2)

    networks = local_response_normalization(networks)
    networks = conv_2d(networks, 256, 3, activation='relu', regularizer="L2")
    networks = max_pool_2d(networks, 2)

    networks = local_response_normalization(networks)
    networks = fully_connected(networks, 512, activation='tanh')
    networks = dropout(networks, 0.8)
    networks = fully_connected(networks, 4092, activation='tanh')
    networks = dropout(networks, 0.8)
    networks = fully_connected(networks, nclass_logos, activation='softmax')
    networks = regression(networks, optimizer='SGD', learning_rate=0.01,
                          loss='categorical_crossentropy', name='target')

    model_logos = tflearn.DNN(networks, tensorboard_verbose=0)
    model_logos.load('logo_128128_150/modeltest_logo.cnn')

    print("LMLF:(Load model logos finished)")
    source = "finished..."
    # return model_logos
    return jsonify({'API Online':source}), 200



@app.route('/logo' ,methods=['POST'])
def model_logos():
    global model_logos
    image = request.get_json()
    img = image['logo']
    im = Image.open(BytesIO(base64.b64decode(img)))
    im.save('777.png', 'PNG')
    im = cv2.imread('777.png')
    width = 128
    height = 128
    dim = (width, height)
    # im = cv2.imread("272.jpg")
    b = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    tmp = b.flatten()
    testX = tmp.reshape([-1, 128, 128, 3])
    result = model_logos.predict(testX)

    # result = model_logos.predict(im)
    # print("This is Result 0 : ", result[0])
    x = np.array(result[0])
    idx = np.argmax(x).tolist()
    return jsonify(idx), 200


    # x = ['{:01.4f}'.format(n) for n in x]
    # x = [float(i) for i in x]
    # y = json.dumps(x)
    # return jsonify({'finis:)': y}), 200
    try:
        os.remove("777.png")
    except: pass


if __name__ == '__main__':
    app.run(debug=True)
