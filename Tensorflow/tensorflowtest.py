
import tensorflow as tf
import numpy as np
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
high = np.array([1,2,3,4,5,6,7],dtype=int)
low = np.array([1,2,3,4,5,6,7], dtype=int)
model.fit(high, low, epochs=500)
print(model.predict([10]))
