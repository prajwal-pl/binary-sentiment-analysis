from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer
import torch
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Load dataset
dataset = load_dataset("json", data_files="data.jsonl", split="train")
tokenizer = AutoTokenizer.from_pretrained("tabularisai/multilingual-sentiment-analysis")

# Filter by split
train_data = dataset.filter(lambda x: x['split'] == 'train')
test_data = dataset.filter(lambda x: x['split'] == 'test')

def tokenize(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

def convert_labels(examples):
    """Convert string labels to integers"""
    labels = []
    for label in examples["label"]:
        if label.lower() == "positive":
            labels.append(1)
        elif label.lower() == "negative":
            labels.append(0)
        else:
            labels.append(0)  # default to negative
    return {"labels": labels}

# Apply tokenization and label conversion
train_data = train_data.map(tokenize, batched=True)
train_data = train_data.map(convert_labels, batched=True)

test_data = test_data.map(tokenize, batched=True)
test_data = test_data.map(convert_labels, batched=True)

# Remove the original 'label' column to avoid confusion
train_data = train_data.remove_columns(['label', 'split'])
test_data = test_data.remove_columns(['label', 'split'])

# Load model with correct number of labels
model = AutoModelForSequenceClassification.from_pretrained(
    "tabularisai/multilingual-sentiment-analysis",
    num_labels=2,
    id2label={0: "negative", 1: "positive"},
    label2id={"negative": 0, "positive": 1},
    ignore_mismatched_sizes=True  # This handles the size mismatch
)

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='binary')
    acc = accuracy_score(labels, predictions)
    
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=3e-5,
    per_device_train_batch_size=4,  # Reduced for stability
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_steps=10,
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    greater_is_better=True,
    seed=42,
    fp16=False,  # CPU training
    max_grad_norm=1.0,  # Gradient clipping
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
    compute_metrics=compute_metrics,
)

print("Starting training...")
print(f"Training samples: {len(train_data)}")
print(f"Test samples: {len(test_data)}")

trainer.train()

# Save the fine-tuned model
print("Saving model to ./model/")
trainer.save_model("./model")
tokenizer.save_pretrained("./model")

print("Fine-tuning completed!")