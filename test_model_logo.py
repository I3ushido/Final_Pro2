import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

nclass_logos = 10
model_logos = None
networks = input_data(shape=[None, 128, 128,3], name='input')
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

