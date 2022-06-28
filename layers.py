# Custom L1 Distance layer module
# WHy do we need this: to load the custom model

# Import dependencies
import tensorflow as tf
from keras.layers import Layer

# Custom L1 distance layer

class L1Dist(Layer):
    def __init__(self, **kwargs):
        super().__init__()
       
    # Magic happens here - similarity calculation
    def call(self, input_embedding, validation_embbedding):
        return tf.math.abs(input_embedding - validation_embbedding)