import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(train_image,train_label),(test_image,test_label)=mnist.load_data()
plt.imshow(train_image[0])


