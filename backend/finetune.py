from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer

dataset = load_dataset("json", data_files="data.jsonl")
tokenizer = AutoTokenizer.from_pretrained("tabularisai/multilingual-sentiment-analysis")

def tokenize(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

dataset = dataset.map(tokenize, batched=True)

model = AutoModelForSequenceClassification.from_pretrained("tabularisai/multilingual-sentiment-analysis", num_labels=5)

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=3e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)

trainer.train()
model.save_pretrained("./finetuned_model")
