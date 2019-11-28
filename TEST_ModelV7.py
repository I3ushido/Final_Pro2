import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
import numpy as np
import cv2




nclass = 4
model=None


network = input_data(shape=[None, 80, 50,1], name='input') 
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
model.load('ModelV7/modeltestDataV7.cnn')


##a = cv2.imread("white.jpg")
a = cv2.imread("test_human/car_61.jpg")
cv2.imshow('read',a)
width = 50
height = 80
dim = (width, height)
b = cv2.resize(a, dim, interpolation = cv2.INTER_AREA)
img_tmp = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
##_ ,img_gray = cv2.threshold(img_tmp,220,255,cv2.THRESH_BINARY)
cv2.imshow('read',img_tmp)
#print(img_gray)
tmp = img_tmp.flatten()
#tmp = b.flatten()
testX = tmp.reshape([-1, 80, 50, 1])
print('This is testX : ',testX)
result = model.predict(testX)
print("This is Result 0 : ",result[0])
x = np.array(result[0])
print('X',x)

idx = np.argmax(x)
print(idx)
if idx == 0:
    print("Car_Type_1")
elif idx == 1:
    print("Car_Type_2")
elif idx == 2:
    print("Car_Type_3")
elif idx == 3:
    print("Other_Car")
    

print('sucess')

