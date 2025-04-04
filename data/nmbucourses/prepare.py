import os
import requests
import tiktoken
import numpy as np

file = "crawled_text.txt"

with open(file, "r") as f:
    data = f.read()

n = len(data)
train_data = data[: int(n * 0.9)]
val_data = data[int(n * 0.9) :]


enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")


train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), "train.bin"))
val_ids.tofile(os.path.join(os.path.dirname(__file__), "val.bin"))