import pandas as pd
from pathlib import Path
import zipfile
import time
import json
Extract_files = False
CLEAN_TEXT = False 
if Extract_files:
    with zipfile.ZipFile('/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/en_words/images.zip','r') as zip:
        zip.extractall('/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/en_words/images/')

 
path = "/home/ngyongyossy/mohammad/Data/DH-Lab_aug/"

if CLEAN_TEXT:
    import re
    with open(f'{path}labels.txt', encoding='utf-8') as fp1:
     with open(f'{path}labels_clean.txt', mode='w', encoding='utf-8') as fp2:
        for row in fp1:
            if row.strip():
                file_text, text = re.split(r'\s{3}', row, maxsplit=1)
                text = re.sub(r'\s+', ' ', text)
                fp2.write(f"{file_text}{' ':4}{text}\n")
    print('File has cleaned ::')

# time.sleep(5)

# df = pd.read_csv(f'{path}labels.txt', # labels_clean.txt
#                  header=None,
#                  delimiter='   ',
#                  encoding="utf8",
#                  error_bad_lines=False,
#                  engine='python',
#                  ) 
# df.rename(columns={0: "file_name", 1: "text"}, inplace=True)
def load_jsonl(path):
    return pd.read_json(
                        path_or_buf = f'{path}all_labels.jsonl',
                        lines=True) 
df = load_jsonl(path)
print(df.head())
print(len(df))
def is_dir_exist(filename): 
    path = "/home/ngyongyossy/mohammad/Data/DH-Lab_aug/"
    path_to_file = f'{path}images/'+ filename # df['file_name'][idx] # 'readme.txt'
    path = Path(path_to_file)
    return path.is_file() 

def drop_row(idx):    
    return df.drop(df.index[idx]) 
list_fn = [
            df['file_name'][idx]
            for idx in range(len(df))
            if not is_dir_exist(df['file_name'][idx])
          ]

print('list of file names that exist in labels but not in imgs dir: \n', list_fn)
for i in list_fn:
    df.drop(df[df['file_name'] == i ].index, inplace = True)

time.sleep(3)
print("Data frame after processed" , df.head(10))

# save resulting df 
reddit = df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
with open(f"{path}all__labels.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
print('ok')
