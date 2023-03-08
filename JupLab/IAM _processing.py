import os
os.environ['CUDA_VISIBLE_DEVICES'] = '5'
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
import argparse
import json

LOAD_LAIA = True
# --------------------------------------
parser = argparse.ArgumentParser(description="Example script for converting Txt or Jsonl file format to Parquet Hungarain Laia as ex.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("working_dir",   help="Location of input file (single text file or Single jsonl file )")

args = parser.parse_args()
print(args)
config = vars(args)

working_dir  = config['working_dir']
# --------------------------------------
def clean_text(input_text: str) -> str:
    text = input_text.replace('+', '-')
    return text.replace('|', ' ')
#---------------------------------------
def load_iam(d) -> pd.DataFrame:
    data = []
    # print(train_text)
    with open(d) as infile:
        for line in infile:
            split = line.strip().split(' ')
            file_name = split[0]
            text = split[-1]
            data.append((file_name, clean_text(text)))

    df = pd.DataFrame(data, columns=['file_name', 'text'])
    df.rename(columns={0: 'file_name', 8: 'text'}, inplace=True)
    df['file_name'] = df['file_name'].apply(lambda x: x + '.png')

    df = df[['file_name', 'text']]
    return df
#-----------------------------------------------------
def load_laia(d) -> pd.DataFrame:
    data = []
    print(d)
    with open(d) as infile:
        for line in infile:
            file_name, _, _, _, _, _, _, _, text = line.strip().split(' ')
            data.append((file_name, clean_text(text)))

    df = pd.DataFrame(data, columns=['file_name', 'text'])
    df.rename(columns={0: 'file_name', 8: 'text'}, inplace=True)
    df['file_name'] = df['file_name'].apply(lambda x: x + '.jpg')
    df = df[['file_name', 'text']]
    return df
#-----------------------------------------------------
#-----------------------------------------------------
if LOAD_LAIA:     
    df = load_laia(f'{working_dir}train.txt')
else:     
    df = load_iam(f'{working_dir}train.txt') 

print(df.head())
print('\n ',df['file_name'][3] ,df['text'][3])
# ------------------------------------------------------
reddit = df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
with open(f"{working_dir}train.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
