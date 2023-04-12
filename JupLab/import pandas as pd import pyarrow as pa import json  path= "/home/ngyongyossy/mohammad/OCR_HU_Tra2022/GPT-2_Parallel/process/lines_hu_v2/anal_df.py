import pandas as pd
import pyarrow as pa
import json

path= "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v2/all_train_v2.jsonl"
def load_jsonl(path):
    return pd.read_json(
                        path_or_buf = f'{path}',
                        lines=True) 

df = load_jsonl(path)
print(df.describe())
print(df.info())
print(df.columns)
print(df.shape)
print(df.head(2))
print(df.tail(2))
