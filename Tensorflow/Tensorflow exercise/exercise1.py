import tensorflow as tf
import numpy as np
from tensorflow import keras

model= keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
bed= np.array([1,2,3,4,5,6],dtype=float)
price= np.array([100,150,200,250,300,350],dtype=float)
model.fit(bed,price,epochs=500)
print(model.predict([7]))

