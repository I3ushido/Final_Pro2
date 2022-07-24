import os, os.path
import numpy as np
import pandas as pd
from scipy.misc import imread, imresize
from sklearn.metrics import accuracy_score
import tensorflow as tf
from PIL import Image
from sklearn.metrics import confusion_matrix
import pylab as pl
from sklearn.metrics import precision_recall_fscore_support as score
#from skimage import io, color
#from showimages import show_images
#from patch import extract_patches2, plot_patches
import tflearn
from sklearn.model_selection import train_test_split
import cv2
def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()
def model_summary():
    model_vars = tf.trainable_variables()
    slim.model_analyzer.analyze_vars(model_vars, print_info=True)


def read_images(fold_path):
    imgs = []
    path = fold_path
    valid_images = [".png"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(imread(os.path.join(path,f)))
    return imgs
##
root_dir = os.path.abspath('img_gray/')
data  = []
label = []
t = os.listdir(root_dir)
################################################
##
i = 0
nclass = 4
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
    b = imresize(a, [80,50])    
    tmp = b.flatten()
    data_fl.append(tmp)
print('Shape : ',b.shape)
X = np.asarray(data_fl)
print(X.shape)
print("loaded train data ...")


X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.20, random_state=42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
print(X_train, X_test)

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

Xtrain = X_train.reshape([-1, 80, 50, 1])
Xtest = X_test.reshape([-1, 80, 50, 1])

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


# Training
model = tflearn.DNN(network, tensorboard_verbose=0)

model.fit({'input': Xtrain}, {'target': y_train}, n_epoch=150,
           validation_set=({'input': Xtest}, {'target': y_test}),
           snapshot_step=1000, show_metric=True, run_id='Car_Type')
model.save('modeltestDataV7.cnn')

##model.load('model25.cnn')
##result = model.evaluate(Xtest,y_test)
##print(result)
##a = cv2.imread("data/data1/11.jpg")
##width = 45
##height = 45
##dim = (width, height)
##b = cv2.resize(a, dim, interpolation = cv2.INTER_AREA)
##tmp = b.flatten()
##testX = tmp.reshape([-1, 45, 45, 1])
##result = model.predict(testX)
###print(result)
##x = np.array(result[0])
##idx = np.argmax(x)
##print(idx)
y_test_non_category = [ np.argmax(t) for t in y_test ]
i=0
Y_pred = []
for a in Xtest:
    height = 80
    width = 50    
    dim = (width, height)
    b = cv2.resize(a, dim, interpolation = cv2.INTER_AREA)
    tmp = b.flatten()
    testX = tmp.reshape([-1, 80, 50, 1])
    result = model.predict(testX)
    #print(result)
    x = np.array(result[0]) 
    idx = np.argmax(x)
##    if idx==2 and y_test_non_category[i]==3:
##        idx=3
##    if idx==3 and y_test_non_category[i]==2:
##        idx=2
    Y_pred.append(idx)
    i=i+1

from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test_non_category, Y_pred)
print(conf_mat)
##print(model.feature_importances_)5
plot_confusion_matrix(cm           = conf_mat, 
                      normalize    = False,
                      target_names = ['Car1', 'Car2', 'Car3','Car4'],
                      title        = "Confusion Matrix,")
