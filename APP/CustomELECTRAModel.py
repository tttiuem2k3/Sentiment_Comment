from transformers import ElectraTokenizer, ElectraModel 
import torch.nn as nn
import torch     # type: ignore
class CustomELECTRAModel(nn.Module):
    def __init__(self, model_name, num_labels=2):
        super(CustomELECTRAModel, self).__init__()
        self.electra = ElectraModel.from_pretrained(model_name)
        self.attention = nn.MultiheadAttention(
            embed_dim=self.electra.config.hidden_size, 
            num_heads=8, 
            batch_first=True
        )
        self.fc1 = nn.Linear(self.electra.config.hidden_size, 128)
        self.fc2 = nn.Linear(128, num_labels)
        self.dropout = nn.Dropout(0.4)
        
        # Thêm lớp LayerNorm
        self.layer_norm = nn.LayerNorm(128)

    def forward(self, input_ids, attention_mask):
        # Trích xuất embeddings từ ELECTRA
        outputs = self.electra(input_ids=input_ids, attention_mask=attention_mask)
        hidden_states = outputs.last_hidden_state  # Shape: (batch_size, seq_len, hidden_size)

        # Attention pooling
        attn_output, _ = self.attention(hidden_states, hidden_states, hidden_states, key_padding_mask=~attention_mask.bool())
        
        # Chọn CLS token làm đặc trưng đại diện
        cls_token_output = attn_output[:, 0, :]  # CLS token tương ứng với đầu tiên của sequence output

        # Fully connected layers
        pooled_output = self.dropout(cls_token_output)  # Áp dụng dropout
        fc1_output = torch.relu(self.fc1(pooled_output))
        
        # Áp dụng Layer Normalization sau FC1
        fc1_output = self.layer_norm(fc1_output)
        
        logits = self.fc2(fc1_output)
        return logits