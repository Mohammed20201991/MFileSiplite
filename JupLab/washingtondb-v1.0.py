import os
os.environ['CUDA_VISIBLE_DEVICES'] = '5'
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
import argparse
import json

Transcription = True 
# --------------------------------------
parser = argparse.ArgumentParser(description="Example script for converting Txt or Jsonl file format to Parquet Hungarain Laia as ex.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("working_dir",   help="Location of input file (single text file or Single jsonl file )")

args = parser.parse_args()
print(args)
config = vars(args)

working_dir  = config['working_dir']
#----------------------------------------
def clean_text(input_text: str) -> str:
    text_0 = input_text.replace('-', '')
    text_1 = text_0.replace('s_pt', '.')
    text_2 = text_1.replace('s_cm', ',')
    text_3 = text_2.replace('s_sq', ';')
    text_4 = text_3.replace('_qo', ':')
    text_5 = text_4.replace('s_mi', '.')
    text_6 = text_5.replace('s_', '')
    return text_6.replace('|', ' ')
#----------------------------------------
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
    # df.rename(columns={0: 'file_name', 8: 'text'}, inplace=True)
    df.rename(columns={0: 'file_name', 1: 'text'}, inplace=True)
    df['file_name'] = df['file_name'].apply(lambda x: x + '.png')

    df = df[['file_name', 'text']]
    return df
#-----------------------------------------------------
#-----------------------------------------------------
if Transcription:     
    df = load_iam(f'{working_dir}transcription.txt') 
else:     
    df = load_iam(f'{working_dir}word_labels.txt') 

print(df.head(10))
print('\n ',df['file_name'][3] ,df['text'][3])
print(df.tail(4))

# -----------------------------------------------------
if Transcription:
    reddit = df.to_dict(orient= "records")
    print(type(reddit) , len(reddit))
    # we have list of dict[{},{},{}]
    with open(f"{working_dir}transcription.jsonl","w") as f: 
        for line in reddit:
            f.write(json.dumps(line,ensure_ascii=False) + "\n")

else:
    reddit = df.to_dict(orient= "records")
    print(type(reddit) , len(reddit))
    # we have list of dict[{},{},{}]
    with open(f"{working_dir}words.jsonl","w") as f: 
        for line in reddit:
            f.write(json.dumps(line,ensure_ascii=False) + "\n") 
