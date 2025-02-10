# ✨ Phân tích Sắc Thái Cảm Xúc Bình Luận Trên Sàn Thương Mại Điện Tử ✨

## 💡 Giới Thiệu Chung
Trong bối cảnh phát triển mạnh mẽ của các sàn thương mại điện tử, các bình luận từ người tiêu dùng trở thành nguồn thông tin quan trọng giúp người mua đồ phân tích sản phẩm và nhà bán hàng cải thiện dịch vụ.

Dự án này nhằm mục tiêu giúp phân tích nhanh các bình luận và tìm hiểu xem nhận định của người dùng là tích cực hay tiêu cực từ đó đưa ra được nhận xét tổng thể là sản phẩm có nên mua hay là không!

**Sentiment Analysis** là một kỹ thuật trong xử lý ngôn ngữ tự nhiên **(NLP)** dùng để xác định và phân loại cảm xúc (tích cực, tiêu cực) của văn bản. Đề tài này tập trung xây dựng một hệ thống phân tích cảm xúc hiệu quả, áp dụng mô hình **PhoBERT** kết hợp với **CNN** và **BiLSTM** để khai thác tối ưu đặc trưng ngữ nghĩa và ngữ cảnh trong bình luận tiếng Việt. Ngoài ra còn triển khai mô hình **ELECTRA-BASE** nhằm đánh giá xem mô hình trên được huấn luyện trên Embedding của PhoBert đã tới hạn với tập dữ liệu hay chưa, triển khai mô hình ELECTRA-Base loại bỏ hoàn toàn các lớp tùy chỉnh (CNN, BiLSTM, Attention) và dựa vào kiến trúc transformer của Electra để xem độ chính xác có được cải thiện hay không, khám phá khả năng của ELECTRA trong xử lý ngôn ngữ tiếng Việt. Nghiên cứu hứa hẹn mang lại giá trị ứng dụng cao và đóng góp vào việc xử lý ngôn ngữ tự nhiên cho tiếng Việt.

---

## 🛠️ Chức năng chính
- **🔍 Phân loại tin giả**: Nhận đầu vào là văn bản, trả về nhãn "Thật"/"Giả" kèm xác suất.
- **📊 Giao diện trực quan**: Biểu đồ pie chart.

---

## :tv: Demo
![Demo](demo1.gif)
- Xem DEMO đầy đủ tại đây: https://www.youtube.com/watch?v=HQ2c8JY_TXI&t=25sz
  
---

## Tổng quan hệ thống và quy trình thực hiện 

 ![Sơ đồ tổng quan hệ thống](./Images/img1.JPG)
 
 ![Sơ đồ qui trình thực hiện](./Images/img2.JPG)
 
---

## 📂 Nguồn dữ liệu
- **📰 Dữ liệu**: Thu thập từ các bình luận của sản phẩm từ các sàn thương mại điện tử như: Shopee, Lazada, Tiki, Sendo,...
- **📊 Cấu trúc dữ liệu**: Bao gồm  nội dung của bình luận, nhãn (Tích cực/Tiêu cực).
---

## 🔄 Quá trình thu thập và xử lý dữ liệu
1. **🗂️ Thu thập dữ liệu**:
   - Sử dụng các thư viện như Selenium, BeautifulSoup, Requests,.. để thu thập dữ liệu là các bài báo từ nguồn dữ liệu theo cấu trúc dữ liệu.
   - Gán nhãn cho dữ liệu: Sau bước thu thập dữ liệu bình luận là gán nhãn (tích cực: 0 , tiêu cực: 1) cho các bình luận dựa theo tiêu chí:
      * Để đánh giá một nhãn của bình luận thì trước hết phải ưu tiên đến chất lượng của sản phẩm, ví dụ:
         
            + Sản phẩm rất đẹp, giao hàng nhanh - Nhãn tích cực: 0
            + Sản phẩm kém chất lượng, giao hàng nhanh - Nhãn tiêu cực: 1
      * Các bình luận trung lập thì phải dựa vào mức độ đánh giá giá sản phẩm để gán nhãn,ví dụ: 
        
            + Sản phẩm tốt, giao hàng hơi chậm - Nhãn tích cực: 0
            + Sản phẩm tốt, giao hàng chậm, đóng gói sản phẩm kém - Nhãn tiêu cực: 1
   - Tham khảo code ở thư mục [Crawl](./DATA/Crawl)
2. **🧹 Tiền xử lý**:
   - Chuẩn hóa văn bản (chuyển chữ thường, xóa ký tự đặc biệt).
   - Tách từ tiếng Việt (word_segmentation): [`NlpHUST/vi-word-segmentation`](https://huggingface.co/NlpHUST/vi-word-segmentation)
   - Loại bỏ stopwords và cân bằng dữ liệu.
     
   ![Qui trình tiền xử lý dữ liệu](./Images/img3.JPG)
3. **📊 Thống kê dữ liệu**:
   
   | Loại bình luận | Số lượng | Tỷ lệ |
   |----------------|----------|-------|
   | 📰 Tích cực   | 17,312   | 50.2% |
   | 📛 Tiêu cực   | 17,156   | 49.8% |

4. **📂 Phân chia tập dữ liệu huấn luyện**:
   - **Train**: 70% (24.127 mẫu)
   - **Validation**: 15% (5.170 mẫu)
   - **Test**: 15% (5.171 mẫu)

---

## 🚀 ELECTRA-Base: Giới thiệu và Sức mạnh
### 🌟 Tổng quan
**ELECTRA** (Efficiently Learning an Encoder that Classifies Token Replacements Accurately) là mô hình NLP sử dụng cơ chế **Replaced Token Detection**:
- **Generator**: Tạo token giả thay thế ngẫu nhiên.
- **Discriminator**: Phát hiện token bị thay thế, tối ưu hóa việc học toàn bộ đầu vào.
  
![cơ chế electra](./Images/img4.jpg)
### 💪 Ưu điểm vượt trội
| Ưu điểm                  | Hiệu quả                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| **💻 Tiết kiệm tài nguyên**     | Chỉ cần 25% tài nguyên so với BERT/RoBERTa                               |
| **📜 Xử lý văn bản dài**        | Áp dụng **Sliding Window** (512 tokens/window) với overlap 128 tokens    |
| **🎯 Độ chính xác cao**         | F1-score đạt **99%** trên tập test                                       |
| **🧠 Tích hợp Attention**       | Thêm Multihead Attention để tập trung vào từ khóa quan trọng            |

### 🔧 Cải tiến trong dự án
1. **📜 Xử lý văn bản dài**:
   - Chia văn bản thành các đoạn 512 tokens, kết hợp kỹ thuật overlap - cửa sổ trượt với độ trượt là 128 tokens.
   - Dùng voting từ các đoạn để quyết định nhãn cuối cùng.
2. **⚙️ Nâng cấp kiến trúc**:
   - Thêm lớp **MultiheadAttention** và **LayerNorm**.
   - Tích hợp Fully Connected layers để tối ưu biểu diễn đặc trưng.
     
![cải tiến mô hình electra](./Images/img5.jpg)

### 🚀 Qui trình huấn luyện
1. **🛠️ Cấu hình huấn luyện:**

| Epochs      | BATH_SIZE | OPTIMIZER | DROPOUT |LEARNING_RATE|NUM_CLASSES| 
|-------------|-----------|-----------|---------|-------------|-----------| 
|    **4**    |  **48**   |**AdamW**  | **0.3** | **5e-5 -> 1e-5**|**2**| 

2. **🗃️ Qui trình huấn luyện:**

![qui trình huấn luyện](./Images/img6.jpg)


## 📈 Kết quả
| Model       | Accuracy | F1-score | Recall |
|-------------|----------|----------|--------|
| ELECTRA-Base| **99%**  | **99%**  | **99%**|

![Ma trận nhầm lẫn](./Images/img9.jpg)

---
## ⚖️ So sánh kết quả với Transformer-XL và PhoBERT

Dưới đây là bảng so sánh kết quả giữa **ELECTRA-Base**, **Transformer-XL**, và **PhoBERT** trên tập dữ liệu test:

| Model           | Accuracy | F1-score | Recall | Parameters |
|-----------------|----------|----------|--------|------------|
| **ELECTRA-Base**| **99%**  | **99%**  | **99%**| 109M       |
| Transformer-XL  | 94%      | 94%      | 94%    | 191M       |
| PhoBERT         | 93%      | 93%      | 93%    | 135M       |

### 📊 Biểu đồ so sánh
![Biểu đồ so sánh độ mất mát](./Images/img7.jpg)

![Biểu đồ so sánh độ chính xác](./Images/img8.jpg)

### 📝 Nhận xét
- **ELECTRA-Base** cho kết quả **vượt trội** so với Transformer-XL và PhoBERT, đạt độ chính xác **99%**.
- **Transformer-XL** và **PhoBERT** cũng cho kết quả tốt, nhưng độ chính xác thấp hơn (94% và 93%).
- **ELECTRA-Base** sử dụng ít tham số hơn (109M) so với Transformer-XL (191M) và PhoBERT (135M), giúp tiết kiệm tài nguyên tính toán.

---
## 🔮 Hướng phát triển
- **🌍 Mở rộng sang đa ngôn ngữ** (tiếng Anh, Trung).
- **🖼️ Tích hợp phân tích hình ảnh/video** bằng CNN.
- **🌐 Xây dựng extension trình duyệt** để quét tin giả real-time.

---

## 🛠️ Cài đặt
### Tải code:
```bash
git clone https://github.com/your-repo/fake-news-detection
cd fake-news-detection
pip install -r requirements.txt
```
### Huấn luyện mô hình:
- Huấn luyện mô hình dựa trên bộ data: [`DATA.rar`](./DATA/DATA.rar)
- Tham khoản code huấn luyện mô hình: [`CODE`](./CODE)
### Chạy ứng dụng:
Run python [`App.py`](./APP/App.py)

---

##  📞 Liên hệ
- 👥 Linkedin: https://www.linkedin.com/in/thinh-tran-04122k3/

- 📧 Email: tttiuem2k3@gmail.com
