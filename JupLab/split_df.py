import pandas as pd
import time 
import json

source_folder      = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/test/'
destination_folder = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/test/"

def load_jsonl(path):
    return pd.read_json(
                        path_or_buf = path,
                        lines=True) 
df = load_jsonl(f'{source_folder}Mix.jsonl')
print(df.head())
 
# n is the number of samples we wanna choose  
test_df = df.sample(frac= 0.1) 
print(len(test_df),test_df.head(3))
#---------------------------------------------------
# Converting new dataframe to jsonl
time.sleep(3)
reddit = test_df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
with open(f"{destination_folder}test.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
# /--------------------------------------------------------

train_df = df.drop(test_df.index) 
time.sleep(3)
reddit = train_df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
with open(f"{destination_folder}train.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
