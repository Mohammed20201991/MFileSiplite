import pandas as pd
from pathlib import Path
import zipfile
Extract_files = False
if Extract_files:
    with zipfile.ZipFile('/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/en_words/images.zip','r') as zip:
        zip.extractall('/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/en_words/images/')

path = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/sample/" 
path2= "/home/ngyongyossy/mohammad/trdghm/TextRecognitionDataGeneratorHuMu23/trdg/out/"
path4= "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/en_words/"

df = pd.read_csv(f'{path4}labels.txt',
                 header=None,
                 delimiter='   ',
                 encoding="utf8",
                 error_bad_lines=False,
                 engine='python'
                 )
df.rename(columns={0: "file_name", 1: "text"}, inplace=True)
print(df.head())
# print(df.tail())
# print(len(df))


def is_dir_exist(filename):
    
    path4= "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/en_words/"
    # path_to_file = f'{path2}imgs/'+ filename # df['file_name'][idx] # 'readme.txt'
    path_to_file = f'{path4}images/en/'+ filename # df['file_name'][idx] # 'readme.txt'

    path = Path(path_to_file)

    # print(path.is_file()) 
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

print("Data frame after processed" , df.head(11))

reddit = df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
import json 
with open("train_en.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
