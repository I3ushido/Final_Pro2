# BattlePass
import PyQt5
import numpy as np
import cv2
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utilsV2
import webcolors
import time

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, \
    QFileDialog, QAction, QMessageBox, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import pyqtSlot, Qt, QSize

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from tensorflow import Graph, Session

import base64
import requests as reqs
from io import BytesIO
from PIL import Image
import pyperclip

global nclass
global model
global nclass_logos
global model_logo


# g1 = tf.Graph()
# g2 = tf.Graph()
#
# with g1.as_default():
#     cnn1 = CNN(..., restore_file='snapshot-model1-10000',..........)
# with g2.as_default():
#     cnn2 = CNN(..., restore_file='snapshot-model2-10000',..........)

def load_logo():
    graph1 = Graph()
    with graph1.as_default():
        session1 = Session()
        with session1.as_default():
            nclass_logos = 10
            model_logos = None
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
            print(model_logos)
            print("LMLF:(Load model logos finished)")
            return model_logos


def load_model():
    graph2 = Graph()
    with graph2.as_default():
        session2 = Session()
        with session2.as_default():
            nclass = 4
            model = None
            network = input_data(shape=[None, 80, 50, 1], name='input')
            network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = conv_2d(network, 128, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = conv_2d(network, 256, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = fully_connected(network, 512, activation='tanh')
            network = dropout(network, 0.8)
            network = fully_connected(network, 4092, activation='tanh')
            network = dropout(network, 0.8)
            network = fully_connected(network, nclass, activation='softmax')
            network = regression(network, optimizer='SGD', learning_rate=0.01,
                                 loss='categorical_crossentropy', name='target')
            model = tflearn.DNN(network, tensorboard_verbose=0)
            model.load('model5/modeltestDataV5.cnn')
            print(model)
            print("LMF:(Load model finished)")
            return model

class Jajah:
    model_logos = load_logo()
    model = load_model()
    print('Hello_UnderWorld.')
    path_image = 'day3-5_1.jpg'
    a = cv2.imread(path_image)
    print("source : {}".format(path_image))
    # cv2.imshow('read', a)
    height = 80
    width = 50
    dim = (width, height)
    b = cv2.resize(a, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow('read', b)
    # print(b)
    tmp = b.flatten()
    testX = tmp.reshape([-1, 80, 50, 1])
    # print('This is testX : ', testX)
    result = model.predict(testX)
    print("This is Result 0 : ", result[0])
    x = np.array(result[0])
    # print('X', x)
    idx = np.argmax(x)
    print(idx)
    if idx == 0:
        print("Car_Type_1")
    elif idx == 1:
        print("Car_Type_2")
    elif idx == 2:
        print("Car_Type_3")
    elif idx == 3:
        print("other_Car")
    else:
        print("Missing Data...")

    im = cv2.imread('272.jpg')
    width = 128
    height = 128
    dim = (width, height)
    # im = cv2.imread("272.jpg")
    b = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)
    tmp = b.flatten()
    testX = tmp.reshape([-1, 128, 128, 3])
    result = model_logos.predict(testX)

    # result = model_logos.predict(im)
    # print("This is Result 0 : ", result[0])
    x = np.array(result[0])
    # print('result[0] : ', result[0])
    x = ['{:01.4f}'.format(n) for n in x]
    x = [float(i) for i in x]
    print('Convert X: ', x)
    idx = np.argmax(x)
    print('idx: ', idx)






