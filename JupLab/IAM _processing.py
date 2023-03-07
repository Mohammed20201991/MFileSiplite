import os
os.environ['CUDA_VISIBLE_DEVICES'] = '5'
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
import argparse


def clean_text(input_text: str) -> str:
    text = input_text.replace('+', '-')
    return text.replace('|', ' ')

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
train_text = "/home/ngyongyossy/mohammad/Data/lines/train.txt"
df = load_iam(train_text) 
print(df.head())
print('\n ',df['file_name'][38] ,df['text'][38])
