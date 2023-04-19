# Importing required libraries
# import pandas as pd
# df = pd.DataFrame(record)
# test_df  = df.sample(frac = 0.5)
# train_df = df.drop(test_df.index)
import pandas as pd
import time 
import json

source_folder      = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/hu_words_v1/'
destination_folder = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/hu_words_v1/"

def load_jsonl(path):
    return pd.read_json(
                        path_or_buf = path,
                        lines=True) 
df = load_jsonl(f'{source_folder}hu_words_train.jsonl')
print(df.head())
 
# n is the number of samples we wanna choose  
test_df = df.sample(frac= 0.05) 
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
with open(f"{destination_folder}hu_words_train.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
