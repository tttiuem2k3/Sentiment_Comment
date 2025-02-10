# --------------------Thêm thư viện cần thiết-----------------------
import torch.nn.functional as F

import numpy as np
import torch     # type: ignore
from transformers import ElectraTokenizer, ElectraModel 
from data_processing import preprocessing_data
# ----------------------Ẩn các cảnh báo vô nghĩa----------------------
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Ẩn các log mức thông tin và cảnh báo của TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' 
import warnings
warnings.filterwarnings("ignore")  # Tắt toàn bộ cảnh báo
from transformers import logging
logging.set_verbosity_error() 
#--------------------------Tải mô hình dự đoán-----------------------------
# Tải tokenizer
tokenizer_path = r'..\TOKENIZER\tokenizer_electra_base'
tokenizer = ElectraTokenizer.from_pretrained(tokenizer_path)

# -------------------------Cấu trúc mô hình----------------------
from CustomELECTRAModel import CustomELECTRAModel
    
# Tải mô hình đã huấn luyện
model_path = r'..\MODEL\sentiment_comment_electra-base_model_v1.pth'
model = torch.load(model_path, map_location=torch.device('cpu'))
# -------------------------Định nghĩa hàm dự đoán nhãn----------------------
class SimplePredictor:
    def __init__(self, model, tokenizer, max_length=128, device='cuda'):
        self.model = model
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.device = device
        
    def predict_label(self, text):
        # Tokenize văn bản với độ dài tối đa
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        input_ids = encoding['input_ids'].to(self.device)
        attention_mask = encoding['attention_mask'].to(self.device)
        
        # Chuyển sang chế độ đánh giá
        self.model.eval()
        with torch.no_grad():
            logits = self.model(input_ids=input_ids, attention_mask=attention_mask)
            
            # Tính xác suất với softmax
            probabilities = F.softmax(logits, dim=-1)
            
            # Lấy nhãn dự đoán và xác suất tương ứng
            prediction = torch.argmax(probabilities, dim=-1).item()
            probability = probabilities[0, prediction].item()
            # Chuẩn hóa lại cho đồng nhất với 2 chương trình thôi
            prob=[]
            prob.append(probability)
        return prediction, prob

device = torch.device('cpu')
# Tạo đối tượng dự đoán
predictor = SimplePredictor(model, tokenizer, max_length=128, device=device)

#------------------------Hàm dự đoán cuối cùng cho một comment--------------------------------
def predict(comment):
    processing_comment = preprocessing_data(comment)
    label, prob = predictor.predict_label(processing_comment)
    
    return processing_comment, label, prob

# --------------------------Test DỰ ĐOÁN--------------------------
# # Ví dụ dự đoán
# example_comment = "Sản phẩm xài oke đấy"
# processing_comment,label,prob=predict(example_comment)
# print(f"Bình luận: \"{example_comment}\"")
# print("\nXử lý comment : ",processing_comment)
# print(f"\nDự đoán nhãn: {'Tích cực' if label == 0 else 'Tiêu cực'}")
# print(f"Xác suất dự đoán: {prob[0]:.4f}")