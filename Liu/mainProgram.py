import os, os.path
import numpy as np
import pandas as pd
from scipy.misc import imread, imresize
from sklearn.metrics import accuracy_score
import tensorflow as tf
from PIL import Image
from sklearn import svm
from sklearn.metrics import confusion_matrix
import pylab as pl
from sklearn.metrics import precision_recall_fscore_support as score
#from skimage import io, color
#from showimages import show_images
#from patch import extract_patches2, plot_patches
import tflearn
from sklearn.model_selection import train_test_split

def read_images(fold_path):
    imgs = []
    path = fold_path
    valid_images = [".jpg"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(imread(os.path.join(path,f)))
    return imgs
##
root_dir = os.path.abspath('Process2/')
data  = []
label = []
t = os.listdir(root_dir)
################################################
##
i = 0
nclass = 3
for a in t :
    data_dir  = os.path.join(root_dir, a)
    #data_fold = os.path.join('Out'+(i+1))
    img = read_images(data_dir)
    print(data_dir)
    l = len(img);
    s = [0]*nclass
    s[i] = 1
    v = [s]*l
    i = i+1
    label.extend(v)
    data.extend(img)
Y = np.asarray(label)
data_fl = [];
#io.imshow(data[5000])
#io.show()

for a in data :
    b = imresize(a, [45,45])
    tmp = b.flatten()
    data_fl.append(tmp)

X = np.asarray(data_fl)
print(X.shape)
print("loaded train data ...")


X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.20, random_state=42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

Xtrain = X_train.reshape([-1, 45, 45, 1])
Xtest = X_test.reshape([-1, 45, 45, 1])

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
network = fully_connected(network, 4096, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, nclass, activation='softmax')
network = regression(network, optimizer='SGD', learning_rate=0.01,
                     loss='categorical_crossentropy', name='target')


# Training
model = tflearn.DNN(network, tensorboard_verbose=0)
model.fit({'input': Xtrain}, {'target': y_train}, n_epoch=100,
           validation_set=({'input': Xtest}, {'target': y_test}),
           snapshot_step=10, show_metric=True, run_id='thai_char')

model.save('modelart.cnn')

#model.load('charmodel.cnn')
#result = model.evaluate(testX,testY)
#print(result)
