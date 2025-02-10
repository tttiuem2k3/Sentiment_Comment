from tensorflow.keras.layers import Layer       # type: ignore
import tensorflow as tf
from transformers import TFAutoModel
class PhoBERTEmbeddingLayer(Layer):
    def __init__(self, pretrained_model_name="vinai/phobert-large", **kwargs):
        super(PhoBERTEmbeddingLayer, self).__init__(**kwargs)
        self.phobert = TFAutoModel.from_pretrained(pretrained_model_name)

    def call(self, inputs, **kwargs):
        input_ids, attention_mask = inputs
        output = self.phobert(input_ids=input_ids, attention_mask=attention_mask)[0]
        return output

    def get_config(self):
        config = super(PhoBERTEmbeddingLayer, self).get_config()
        return config