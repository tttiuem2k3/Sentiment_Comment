import matplotlib.pyplot as plt
import numpy as np

# Kết quả mô hình CNN_BiLSTM
# CNN_BiLSTM_train_accuracy = [0.6016, 0.8102, 0.8261, 0.8509, 0.8620, 0.8825, 0.8982, 0.9172, 0.9344, 0.9486, 0.9557, 0.9616, 0.9715, 0.9775, 0.9813, 0.9834, 0.9875, 0.9876, 0.9911, 0.9925]
# CNN_BiLSTM_train_loss = [6.3496, 5.4116, 4.2626, 2.9268, 1.7723, 1.0304, 0.6526, 0.4456, 0.3137, 0.2324, 0.1897, 0.1506, 0.1154, 0.0937, 0.0774, 0.0661, 0.0543, 0.0520, 0.0406, 0.0362]
# CNN_BiLSTM_val_accuracy = [0.8029, 0.8550, 0.8722, 0.8853, 0.8820, 0.9016, 0.9078, 0.9182, 0.9335, 0.9286, 0.9459, 0.9488, 0.9431, 0.9025, 0.9453, 0.9530, 0.9462, 0.9513, 0.9522, 0.9480]
# CNN_BiLSTM_val_loss = [5.7102, 4.5622, 3.2403, 1.9991, 1.1592, 0.7077, 0.5019, 0.3757, 0.2741, 0.2567, 0.2126, 0.2071, 0.2082, 0.3267, 0.1761, 0.1699, 0.1923, 0.1729, 0.2022, 0.2285]
CNN_BiLSTM_train_accuracy = [
    0.6335, 0.8082, 0.8285, 0.8551, 0.8600, 
    0.8820, 0.9059, 0.9191, 0.9358, 0.9536, 
    0.9622, 0.9688, 0.9708, 0.9796, 0.9795, 
    0.9864, 0.9860, 0.9882, 0.9895, 0.9895
]

CNN_BiLSTM_train_loss = [
    6.3186, 5.4463, 4.3276, 2.9642, 1.7759, 
    1.0071, 0.6221, 0.4252, 0.3026, 0.2195, 
    0.1727, 0.1347, 0.1158, 0.0885, 0.0801, 
    0.0606, 0.0565, 0.0504, 0.0432, 0.0431
]

CNN_BiLSTM_val_accuracy = [
    0.8406, 0.8605, 0.8725, 0.8445, 0.8613, 
    0.8344, 0.9068, 0.9323, 0.9408, 0.9447, 
    0.9453, 0.9464, 0.9532, 0.9534, 0.9536, 
    0.9503, 0.9439, 0.9580, 0.9592, 0.9594
]

CNN_BiLSTM_val_loss = [
    5.6411, 4.6104, 3.2834, 2.1431, 1.1831, 
    0.8946, 0.4755, 0.3324, 0.2771, 0.2165, 
    0.1989, 0.1827, 0.1774, 0.1539, 0.1759, 
    0.1808, 0.2436, 0.1839, 0.1697, 0.1693
]
# Kết quả mô hình ELECTRA-Base
# ELECTRA_train_accuracy = [0.7894, 0.8789, 0.9282, 0.9554, 0.9711, 0.9792, 0.9839, 0.9867, 0.9905, 0.9910, 0.9934, 0.9942]
# ELECTRA_train_loss = [0.4355, 0.2725, 0.1765, 0.1189, 0.0784, 0.0609, 0.0472, 0.0365, 0.0277, 0.0272, 0.0185, 0.0165]
# ELECTRA_val_accuracy = [0.8232, 0.8836, 0.9354, 0.9389, 0.9555, 0.9553, 0.9598, 0.9588, 0.9600, 0.9600, 0.9609, 0.9621]
# ELECTRA_val_loss = [0.3549, 0.2854, 0.1580, 0.1823, 0.1449, 0.1629, 0.1407, 0.1782, 0.1623, 0.1653, 0.1689, 0.1608]
ELECTRA_train_accuracy = [
    0.7819, 0.8764, 0.9244, 0.9493, 0.9685, 
    0.9755, 0.9839, 0.9868, 0.9907, 0.9924, 
    0.9936, 0.9947, 0.9951, 0.9960, 0.9958, 
    0.9960, 0.9974, 0.9971, 0.9973, 0.9972
]

ELECTRA_train_loss = [
    0.4338, 0.2725, 0.1842, 0.1290, 0.0865, 
    0.0666, 0.0472, 0.0383, 0.0284, 0.0232, 
    0.0204, 0.0158, 0.0147, 0.0134, 0.0133, 
    0.0117, 0.0089, 0.0083, 0.0070, 0.0080
]

ELECTRA_val_accuracy = [
    0.8120, 0.9186, 0.9362, 0.9509, 0.9590, 
    0.9588, 0.9605, 0.9561, 0.9636, 0.9611, 
    0.9650, 0.9656, 0.9619, 0.9611, 0.9636, 
    0.9615, 0.9619, 0.9629, 0.9644, 0.9634
]

ELECTRA_val_loss = [
    0.3489, 0.2115, 0.1772, 0.1451, 0.1327, 
    0.1450, 0.1281, 0.1711, 0.1663, 0.1644, 
    0.1628, 0.1801, 0.1776, 0.1786, 0.1840, 
    0.1809, 0.2002, 0.1910, 0.1946, 0.1921
]

# # Kết quả mô hình ELECTRA-Large
# ELECTRA_Large_train_accuracy = [0.7208, 0.8631, 0.9104, 0.9410, 0.9621, 0.9720, 0.9809, 0.9856, 0.9884, 0.9902, 0.9920, 0.9954]
# ELECTRA_Large_train_loss = [0.5260, 0.3072, 0.2089, 0.1458, 0.1034, 0.0746, 0.0549, 0.0405, 0.0335, 0.0283, 0.0219, 0.0150]
# ELECTRA_Large_val_accuracy = [0.8460, 0.8988, 0.9327, 0.9280, 0.9501, 0.9600, 0.9574, 0.9464, 0.9598, 0.9611, 0.9638, 0.9592]
# ELECTRA_Large_val_loss = [0.3442, 0.2373, 0.1735, 0.1987, 0.1439, 0.1505, 0.1529, 0.1986, 0.1649, 0.1699, 0.1819, 0.1963]


#-----------------------------------vẽ so sánh 2 mô hình--------------------------------------------
# # Tạo mảng epoch
# # Số epochs
epochs_CNN_BiLSTM = np.arange(1, len(CNN_BiLSTM_train_loss) + 1)
epochs_ELECTRA = np.arange(1, len(ELECTRA_train_loss) + 1)

# Hàm vẽ biểu đồ với nhãn ở cuối đường
def plot_graph_with_labels(x1, y1, label1, x2, y2, label2, xlabel, ylabel, title):
    plt.figure(figsize=(12, 6))
    plt.plot(x1, y1, label=label1, linestyle='-', marker='o')
    plt.plot(x2, y2, label=label2, linestyle='-', marker='o', linewidth=2, color='red')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    
    
    # Tự động điều chỉnh offset dựa trên khoảng cách
    offset_x_label1 = (x1[-1] - x1[-2]) * 0.2  # Dịch sang phải theo khoảng cách giữa hai điểm cuối
    offset_y_label1 = (y1[-1] - y1[-2]) * 0.2  # Dịch lên theo khoảng cách giữa hai điểm cuối
    offset_x_label2 = (x2[-1] - x2[-2]) * 0.2  # Dịch sang phải tương ứng cho nhãn 2
    offset_y_label2 = (y2[-1] - y2[-2]+0.005) * 1  # Dịch lên cho nhãn 2

    plt.text(
        x1[-1] + offset_x_label1, y1[-1] + offset_y_label1, 
        label1, color='blue', fontsize=12
    )
    plt.text(
        x2[-1] + offset_x_label2, y2[-1] + offset_y_label2, 
        label2, color='red', fontsize=12
    )
    plt.show()
# Train Accuracy
plot_graph_with_labels(
    epochs_CNN_BiLSTM, CNN_BiLSTM_train_accuracy, "  PhoBert_CNN_BiLSTM",
    epochs_ELECTRA, ELECTRA_train_accuracy, "  ELECTRA-Base",
    "Epochs", "Accuracy", "Comparison of Train Accuracy"
)

# Train Loss
plot_graph_with_labels(
    epochs_CNN_BiLSTM, CNN_BiLSTM_train_loss, "  PhoBert_CNN_BiLSTM",
    epochs_ELECTRA, ELECTRA_train_loss, "  ELECTRA-Base",
    "Epochs", "Loss", "Comparison of Train Loss"
)

# Validation Accuracy
plot_graph_with_labels(
    epochs_CNN_BiLSTM, CNN_BiLSTM_val_accuracy, "  PhoBert_CNN_BiLSTM",
    epochs_ELECTRA, ELECTRA_val_accuracy, "  ELECTRA-Base",
    "Epochs", "Accuracy", "Comparison of Validation Accuracy"
)

# Validation Loss
plot_graph_with_labels(
    epochs_CNN_BiLSTM, CNN_BiLSTM_val_loss, "  PhoBert_CNN_BiLSTM",
    epochs_ELECTRA, ELECTRA_val_loss, "  ELECTRA-Base",
    "Epochs", "Loss", "Comparison of Validation Loss"
)
#-----------------------------------vẽ so sánh 3 mô hình--------------------------------------------
# # Mảng epochs
# epochs_CNN_BiLSTM = np.arange(1, len(CNN_BiLSTM_train_loss) + 1)
# epochs_ELECTRA = np.arange(1, len(ELECTRA_train_loss) + 1)
# epochs_ELECTRA_Large = np.arange(1, len(ELECTRA_Large_train_loss) + 1)

# # Hàm vẽ biểu đồ với nhãn ở cuối đường
# def plot_graph_with_labels(x1, y1, label1, x2, y2, label2, x3, y3, label3, xlabel, ylabel, title):
#     plt.figure(figsize=(12, 6))
#     plt.plot(x1, y1, label=label1, linestyle='-', marker='o', linewidth=2, color='blue')
#     plt.plot(x2, y2, label=label2, linestyle='-', marker='o', linewidth=2, color='red')
#     plt.plot(x3, y3, label=label3, linestyle='-', marker='o', linewidth=2, color='green')
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.title(title)
#     plt.legend()
#     plt.grid(True)
    
#     # Thêm nhãn ở cuối mỗi đường
#     plt.text(x1[-1], y1[-1], label1, color='blue', fontsize=12)
#     plt.text(x2[-1], y2[-1], label2, color='red', fontsize=12)
#     plt.text(x3[-1], y3[-1], label3, color='green', fontsize=12)
#     plt.show()

# # Train Accuracy
# plot_graph_with_labels(
#     epochs_CNN_BiLSTM, CNN_BiLSTM_train_accuracy, "  PhoBert_CNN_BiLSTM",
#     epochs_ELECTRA, ELECTRA_train_accuracy, "  ELECTRA-Base",
#     epochs_ELECTRA_Large, ELECTRA_Large_train_accuracy, "  ELECTRA-Large",
#     "Epochs", "Accuracy", "Comparison of Train Accuracy"
# )

# # Train Loss
# plot_graph_with_labels(
#     epochs_CNN_BiLSTM, CNN_BiLSTM_train_loss, "  PhoBert_CNN_BiLSTM",
#     epochs_ELECTRA, ELECTRA_train_loss, "  ELECTRA-Base",
#     epochs_ELECTRA_Large, ELECTRA_Large_train_loss, "  ELECTRA-Large",
#     "Epochs", "Loss", "Comparison of Train Loss"
# )

# # Validation Accuracy
# plot_graph_with_labels(
#     epochs_CNN_BiLSTM, CNN_BiLSTM_val_accuracy, "  PhoBert_CNN_BiLSTM",
#     epochs_ELECTRA, ELECTRA_val_accuracy, "  ELECTRA-Base",
#     epochs_ELECTRA_Large, ELECTRA_Large_val_accuracy, "  ELECTRA-Large",
#     "Epochs", "Accuracy", "Comparison of Validation Accuracy"
# )

# # Validation Loss
# plot_graph_with_labels(
#     epochs_CNN_BiLSTM, CNN_BiLSTM_val_loss, "  PhoBert_CNN_BiLSTM",
#     epochs_ELECTRA, ELECTRA_val_loss, "  ELECTRA-Base",
#     epochs_ELECTRA_Large, ELECTRA_Large_val_loss, "  ELECTRA-Large",
#     "Epochs", "Loss", "Comparison of Validation Loss"
# )
