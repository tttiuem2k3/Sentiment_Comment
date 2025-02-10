# --------------------Thêm thư viện cần thiết-----------------------
from transformers import AutoTokenizer
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model      # type: ignore
from tensorflow.keras.layers import Add             # type: ignore
from data_processing import preprocessing_data
# ----------------------Ẩn các cảnh báo vô nghĩa----------------------
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Ẩn các log mức thông tin và cảnh báo của TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' 
import warnings
warnings.filterwarnings("ignore")  # Tắt toàn bộ cảnh báo
from transformers import logging
logging.set_verbosity_error() 
#--------------------Hiển thị các phiên bản của thư viện----------------
# import keras
# print("\nKeras version:",keras.__version__)
# import tf_keras
# print("TF-Keras version:",tf_keras.__version__)
# import transformers
# print("Transformers version:",transformers.__version__)
# import tensorflow as tf
# import torch
# print("TensorFlow version:", tf.__version__)
# print("PyTorch version:", torch.__version__)
#--------------------------Tải mô hình dự đoán-----------------------------
# Tải tokenizer
tokenizer = AutoTokenizer.from_pretrained(r"..\TOKENIZER\tokenizer_phobert_large")

# Định nghĩa lại PhoBERTEmbeddingLayer nếu cần
from PhoBERTEmbeddingLayer import PhoBERTEmbeddingLayer

# Tải mô hình
model = load_model(r"..\MODEL\sentiment_comment_model_cnn_bilstm_v2.keras", 
                custom_objects={'PhoBERTEmbeddingLayer': PhoBERTEmbeddingLayer,
                'Add': Add})

# Định nghĩa hàm tokenizer data đầu vào của mô hình
def preprocess_comment(comment, tokenizer, max_length=128):
    inputs = tokenizer(
        comment,
        max_length=max_length,
        padding="max_length",
        truncation=True,
        return_tensors="np"
    )
    input_ids = tf.convert_to_tensor(inputs["input_ids"])  # Chuyển thành TensorFlow Tensor
    attention_mask = tf.convert_to_tensor(inputs["attention_mask"])  # Chuyển thành TensorFlow Tensor
    return input_ids, attention_mask
# Định nghĩa hàm dự đoán cho mỗi comment
def predict_comment(comment, model, tokenizer, max_length=128):
    input_ids, attention_mask = preprocess_comment(comment, tokenizer, max_length)
    inputs = {"input_ids": input_ids, "attention_mask": attention_mask}
    prediction = model.predict(inputs)
    label = int(prediction[0][0] > 0.5)  # Chuyển xác suất thành nhãn nhị phân
    if label==0:
        prob=(1-prediction[0])
    else:
        prob=prediction[0]
    return label, prob

#------------------------Hàm dự đoán cuối cùng cho một comment--------------------------------
def predict(comment):
    processing_comment= preprocessing_data(comment)
    label, prob = predict_comment(processing_comment, model, tokenizer)
    return processing_comment,label,prob


#--------------------------Test DỰ ĐOÁN--------------------------
# Ví dụ dự đoán
# example_comment = "Sản phẩm xài oke đấy"
# processing_comment,label,prob=predit(example_comment)
# print(f"Bình luận: \"{example_comment}\"")
# print("\nXử lý comment : ",processing_comment)
# print(f"\nDự đoán nhãn: {'Tích cực' if label == 0 else 'Tiêu cực'}")
# print(f"Xác suất dự đoán: {prob[0]:.4f}")