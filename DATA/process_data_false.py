import pandas as pd
from sklearn.utils import shuffle
import tkinter as tk
from tkinter import messagebox

# Đọc dữ liệu
mismatch_samples = pd.read_csv("mismatch_samples.csv")
mismatch_samples["True Label"] = mismatch_samples["True Label"].astype(int)
mismatch_samples["Predicted Label"] = mismatch_samples["Predicted Label"].astype(int)

test_data = pd.read_csv("dataset_process.csv")
test_data['comment'] = test_data['comment'].astype(str)
test_data['label'] = test_data['label'].astype(int)

data_v3 = pd.read_csv("dataset.csv")
data_v3['comment'] = data_v3['comment'].astype(str)
data_v3['label'] = data_v3['label'].astype(int)


# Khởi tạo danh sách để lưu dữ liệu cập nhật
updated_labels = test_data['label'].tolist()
augmented_data = []  # Lưu dữ liệu nhân bản

# Tạo giao diện với Tkinter
current_index = 0  # Vị trí hiện tại trong mismatch_samples

def log_to_file(message):
    try:
        # Mở file check.txt để đọc toàn bộ nội dung
        with open("check.txt", "r", encoding="utf-8") as file:
            existing_lines = file.readlines()
        
        # Kiểm tra xem message đã có trong file chưa
        if f"{message}\n" not in existing_lines:
            # Nếu chưa có, mở file check.txt theo chế độ ghi tiếp
            with open("check.txt", "a", encoding="utf-8") as file:
                file.write(message + "\n")
    except FileNotFoundError:
        # Nếu file chưa tồn tại, tạo mới và ghi dòng message vào file
        with open("check.txt", "a", encoding="utf-8") as file:
            file.write(message + "\n")
        
def update_label(choice):
    global current_index
    sample = mismatch_samples.iloc[current_index]
    idx = int(sample["Index"])
    test_row = test_data.iloc[idx]

    if choice == "change":  # Đổi nhãn
        updated_labels[idx] = 1 - test_row['label'] 
        log_to_file(f"Comment thứ {idx} đã bấm nút Xanh")
        # messagebox.showinfo("Info", "Label updated.")
    else:
        
        for _ in range(5):  # Nhân bản dữ liệu
            augmented_data.append({"comment": test_row['comment'], "label": test_row['label']})
        log_to_file(f"Comment thứ {idx} đã bấm nút Đỏ")
        # messagebox.showinfo("Info", "Data augmented 5 times.")

    current_index += 1
    if current_index >= len(mismatch_samples):
        save_and_exit()
    else:
        display_sample()


def display_sample():
    sample = mismatch_samples.iloc[current_index]
    idx = int(sample["Index"])
    test_row = test_data.iloc[idx]
    # data_row = data_v3.iloc[idx]
    # Cập nhật nội dung các nhãn
    text_label.config(text=f"Comment {idx} gốc: {sample['Text']}")
    true_label_label.config(text=f"True Label: {'Positive' if sample['True Label'] == 0 else 'Negative'}")
    pred_label_label.config(text=f"Predicted Label: {'Positive' if sample['Predicted Label'] == 0 else 'Negative'}")
    original_label_label.config(text=f"Label gốc: {'Positive' if test_row['label'] == 0 else 'Negative'}")

    # Xóa và thêm mới nội dung trong widget Text
    test_comment_label.delete("1.0", tk.END)
    test_comment_label.insert(tk.END, f"Comment {idx} đã xử lý: {test_row['comment']}")

    # Thay đổi màu nền của cửa sổ dựa trên Label gốc
    if test_row['label'] == 0:  # Positive
        root.configure(bg="#d4edda")  # Xanh lá cây nhạt
    else:  # Negative
        root.configure(bg="#f8d7da")  # Đỏ nhạt


def save_and_exit():
    # Cập nhật tập test ban đầu
    test_data['label'] = updated_labels

    # Tạo DataFrame từ dữ liệu nhân bản
    augmented_df = pd.DataFrame(augmented_data)

    # Gộp dữ liệu đã nhân bản vào tập test
    final_data = pd.concat([test_data, augmented_df], ignore_index=True)

    # Xáo trộn dữ liệu
    final_data = shuffle(final_data, random_state=42)

    # Lưu dữ liệu cập nhật ra file mới
    output_path = "dataset_process_v5.csv"
    final_data.to_csv(output_path, index=False, encoding='utf-8')
    messagebox.showinfo("Completed", f"Updated and augmented data saved to {output_path}.")
    root.destroy()


# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Label Update Tool")
root.geometry("800x600")  # Đặt kích thước cửa sổ (rộng x cao)
root.configure(bg="#f0f0f0")  # Màu nền chính của cửa sổ

# Các widget giao diện
text_label = tk.Label(root, text="", wraplength=750, justify="left", fg="#333333", bg="#f0f0f0", font=("Arial", 14, "bold"))
text_label.pack(pady=10)

true_label_label = tk.Label(root, text="", fg="#006400", bg="#f0f0f0", font=("Arial", 12))
true_label_label.pack()

pred_label_label = tk.Label(root, text="", fg="#8B0000", bg="#f0f0f0", font=("Arial", 12))
pred_label_label.pack()

# Dùng Text widget để hiển thị comment dài
test_comment_label = tk.Text(root, height=8, wrap="word", fg="#333333", bg="#f0f0f0", font=("Arial", 12), bd=0)
test_comment_label.pack(pady=10)

original_label_label = tk.Label(root, text="", fg="#1E90FF", bg="#f0f0f0", font=("Arial", 12, "italic"))
original_label_label.pack()

# Các nút lựa chọn
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

change_label_button = tk.Button(
    button_frame, text="Change Label", command=lambda: update_label("change"), bg="#4CAF50", fg="white", font=("Arial", 12),
    activebackground="#45a049", activeforeground="white", padx=15, pady=8
)
change_label_button.pack(side="left", padx=20)

keep_label_button = tk.Button(
    button_frame, text="Keep Label", command=lambda: update_label("keep"), bg="#f44336", fg="white", font=("Arial", 12),
    activebackground="#e53935", activeforeground="white", padx=15, pady=8
)
keep_label_button.pack(side="left", padx=20)

# Hiển thị mẫu đầu tiên
display_sample()

# Chạy giao diện
root.mainloop()
