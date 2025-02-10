# import pandas as pd
# # # check file utf 8
# import csv

# def check_utf8(input_file):
#     try:
#         with open(input_file, 'r', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             for line_number, row in enumerate(reader, start=1):
#                 try:
#                     str(row)  # Kiểm tra từng dòng có phải UTF-8
#                 except UnicodeDecodeError:
#                     print(f"Dòng {line_number} không phải định dạng UTF-8: {row}")
#     except UnicodeDecodeError as e:
#         print(f"Tệp không phải định dạng UTF-8. Chi tiết lỗi: {e}")

# # Đường dẫn tệp
# input_file = 'dataset_process_v4_final.csv'
# check_utf8(input_file)
# không hiện gì là oke

#--------------------------------------------------------------------------
import pandas as pd
# Đọc dữ liệu từ file CSV gốc
file_path1 = 'dataset_process.csv'
data_df = pd.read_csv(file_path1)
data_positive_df = data_df[data_df['label'] == 0]
data_negative_df = data_df[data_df['label'] == 1]
print("Thông tin dữ liệu gốc")
print("Số mẫu tích cực gốc: ",len(data_positive_df))
print("Số mẫu tiêu cực gốc: ",len(data_negative_df))
# data_positive_df.to_csv('positive.csv', index=False, encoding='utf-8')
# data_negative_df.to_csv('negative.csv', index=False, encoding='utf-8')

# # Đọc dữ liệu từ file CSV đã xử lý tích cực 
# file_path2 = 'dataset_pos_process.csv'
# data_pos_df = pd.read_csv(file_path2)
# # Lọc dữ liệu đã xử lý có label là 0 (Tích cực) và 1 (Tiêu cực)
# data_positive_process1_df = data_pos_df[data_pos_df['label'] == 0]
# data_negative_process1_df = data_pos_df[data_pos_df['label'] == 1]
# print("\nThông tin dữ liệu xử lý tích cực!")
# print(f"Số mẫu tích cực đã xử lý: {len(data_positive_process1_df)} giảm xuống {len(data_positive_df) - len(data_positive_process1_df)} mẫu")
# print(f"Số mẫu tiêu cực tăng lên thành {len(data_negative_process1_df)} mẫu")

# data_positive_process1_df.to_csv('positive.csv', index=False, encoding='utf-8')

# # Sử dụng tập hợp (set) để tăng hiệu suất kiểm tra
# existing_comments = set(data_negative_df['comment'])

# # Tạo DataFrame mới chỉ chứa các dòng không tồn tại trong data_negative_df
# missing_comments_df = data_negative_process1_df[~data_negative_process1_df['comment'].isin(existing_comments)]
# print("Số mẫu tiêu cực tăng lên:",len(missing_comments_df))
# # Lưu các dòng không tồn tại vào file add_negative.csv
# # missing_comments_df[['comment', 'label']].to_csv('add_negative.csv', index=False, encoding='utf-8')

# # Đọc dữ liệu từ file CSV đã xử lý tiêu cực
# file_path3 = 'dataset_neg_process.csv'
# data_neg_df = pd.read_csv(file_path3)
# # Lọc dữ liệu đã xử lý có label là 0 (Tích cực) và 1 (Tiêu cực)
# data_positive_process2_df = data_neg_df[data_neg_df['label'] == 0]
# data_negative_process2_df = data_neg_df[data_neg_df['label'] == 1]
# print("\nThông tin dữ liệu xử lý tiêu cực")
# print(f"Số mẫu tích cực tăng lên thành {len(data_positive_process2_df)} mẫu")
# print(f"Số mẫu tiêu cực đã xử lý: {len(data_negative_process2_df)} giảm xuống {len(data_negative_df) - len(data_negative_process2_df)} mẫu")

# # data_negative_process2_df.to_csv('negative.csv', index=False, encoding='utf-8')

# existing_comments1 = set(data_positive_df['comment'])

# missing_comments_df1 = data_positive_process2_df[~data_positive_process2_df['comment'].isin(existing_comments1)]
# print("Số mẫu đã tích cực tăng lên: ",len(missing_comments_df1))

# missing_comments_df1[['comment', 'label']].to_csv('add_positive.csv', index=False, encoding='utf-8')

#--------------------------------------------------------------------------------------
# import pandas as pd
# from sklearn.utils import shuffle

# # Đọc dữ liệu từ file CSV đã xử lý tích cực
# file_path1 = 'positive_process.csv'
# data_pos_df = pd.read_csv(file_path1)

# # Đọc dữ liệu từ file CSV đã xử lý tiêu cực
# file_path2 = 'negative_process.csv'
# data_neg_df = pd.read_csv(file_path2)

# # Ghép 2 DataFrame lại với nhau
# merged_data = pd.concat([data_pos_df, data_neg_df], ignore_index=True)

# # Xáo trộn các hàng
# shuffled_data = shuffle(merged_data, random_state=42)

# # Kiểm tra dữ liệu sau khi xáo trộn
# print(shuffled_data.head())
# print(shuffled_data.tail())

# # Lưu lại file đã xáo trộn
# shuffled_data.to_csv('dataset_process_v3.csv', index=False)
# #-----------------------------------------------------------------
# #--------------------------------------------------------------------------
# import pandas as pd

# # Đọc dữ liệu từ file CSV gốc
# file_path1 = 'dataset_v3.csv'
# data_df = pd.read_csv(file_path1)

# # Tạo hàm để đếm số từ trong một chuỗi
# def word_count(text):
#     return len(str(text).split())

# # Lọc các dòng có số từ lớn hơn 200 trong cột 'comment'
# filtered_data = data_df[data_df['comment'].apply(word_count) > 150]

# # In ra kết quả
# print(filtered_data[['comment']])

