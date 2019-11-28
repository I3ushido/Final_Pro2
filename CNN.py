import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
import numpy as np
import cv2

nclass = 4
model=None



network = input_data(shape=[None, 45, 45,1], name='input')
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
model.load('mo/modeltest.cnn')


a = cv2.imread("406.png")
cv2.imshow('read', a)
width = 45
height = 45
dim = (width, height)
b = cv2.resize(a, dim, interpolation = cv2.INTER_AREA)
tmp = b.flatten()
testX = tmp.reshape([-1, 45, 45, 1])
result = model.predict(testX)
print(result)
x = np.array(result[0])
idx = np.argmax(x)
print(idx)
print('sucess')

