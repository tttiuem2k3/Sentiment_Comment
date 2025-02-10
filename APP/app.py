from flask import Flask, request, render_template

# ------------Tải mô hình CNN + BiLSTM-----------
from run_model_cnn_bilstm import predict

#-------- Tải mô hình electra----------------
# from CustomELECTRAModel import CustomELECTRAModel
# from run_model_electra import predict

#------Tải chương trình thu thập bình luận từ link sản phẩm-------
from crawl_data_comment_lazada import craw_list_comment

def muc_do(probability):
    if probability <= 0.6:
        return "1"
    elif 0.6<probability <= 0.7:
        return "2"
    elif 0.6<probability <= 0.8:
        return "3"
    elif 0.6<probability <= 0.9:
        return "4"
    else:
        return "5"
def result_for_product(bulk_results):
    # Tính toán số lượng tích cực và tiêu cực
    positive_count = sum(1 for result in bulk_results if result["result"] == "Tích cực")
    negative_count = sum(1 for result in bulk_results if result["result"] == "Tiêu cực")

    # Tính tỷ lệ
    total_count = positive_count + negative_count
    positive_ratio = positive_count / total_count if total_count > 0 else 0
    negative_ratio = negative_count / total_count if total_count > 0 else 0
    
    # Xác định kết quả chung
    if positive_count > negative_count:
        result ="Tích cực"
        comment="Đã check ✅: 🆗🆗🆗 👉 Sản phẩm tốt, nên mua! 🙆💪👌🤞💗💯💁👏💐 👉 Xem phân tích chi tiết ở bên dưới!!! 👇👇👇"
        probability=positive_ratio*100
    elif negative_count > positive_count:
        result ="Tiêu cực"
        comment="Đã check ✅: ❌❌❌ 👉 Sản phẩm dỏm, khỏi mua! 🙅🙅🙅❎❌🙏🙌👊👊 Xem phân tích chi tiết ở bên dưới!!! 👇👇👇"
        probability=negative_ratio*100
    else:
        result ="Tích cực"
        comment="Đã check ✅: 🤜🤛 👉 Sản phẩm bình thường, bạn mua hay không tùy bạn! 🤝🌷✌ Xem phân tích chi tiết ở bên dưới!!! 👇👇👇"
        probability=50
    return comment,result,probability

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    comment = None
    result = None
    product_info = None
    probability = None
    bulk_results = []
    if request.method == "POST":
        # Xử lý dự đoán cho 1 bình luận
        comment = request.form.get("comment")
        if comment.startswith("https://")==0:
            print("\nBình luận: ", comment)
            # Giả lập kết quả dự đoán
            # process_comment, label, prob = "xxxxxxx", 1, [0.53231]
            process_comment,label, prob =predict(comment)
            print("\nBình luận đã xử lý: ", process_comment)
            result = "Tích cực" if label == 0 else "Tiêu cực"
            probability = prob[0]*100
        else :
            link = request.form.get("comment")
            product_info,comments_list=craw_list_comment(link)
            # Giả lập kết quả dự đoán
            # comments_list=["dsds","XXXX","asas","dsada","sdscs","đáasdasd"]
            if not product_info and not comments_list:
                comment="Không tìm thấy bình luận trên sản phẩm"
                result="Tiêu cực"
                probability=50
            else:  
                for comment in comments_list:
                    # Giả lập kết quả dự đoán
                    # process_comment, label, prob = "xxxxxxx", 0, [0.84712]
                    process_comment,label, prob =predict(comment)
                    bulk_results.append({
                        "comment": comment.strip(),
                        "result": "Tích cực" if label == 0 else "Tiêu cực",
                        "probability": muc_do(prob[0])
                    })
                    comment,result,probability=result_for_product(bulk_results)
    if probability:
        probability=round(probability, 2) 
    return render_template("index.html", product=product_info,comment=comment, result=result, probability=probability, bulk_results=bulk_results)

if __name__ == "__main__":  
    app.run(debug=True)

#-------------------Chạy chương trình này-----------------------
run_CNN_biLSTM=r"""

$env:PYTHONPATH="D:\TTT_App\Anaconda\Lib\site-packages"
$env:FLASK_APP="app.py"
flask run

"""
