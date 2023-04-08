import pandas as pd
import json
import argparse
parser = argparse.ArgumentParser(description="Example script for converting Txt or Jsonl file format to Parquet",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("input_path1",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path2",   help="Location of input file (single text file or Single jsonl file )")
args = parser.parse_args()
print(args)
config = vars(args)

input_file1  = config['input_path1']   # path to df1
input_file2  = config['input_path2']   # path to df2 
# read df1 
# read df2
# put all df(s) in list frame= [df1,df2]
# use concat method 


def load_jsonl_1():
    return pd.read_json(
                        path_or_buf = f'{input_file1}train.jsonl',
                        lines=True) 
df1 = load_jsonl_1()
print(df1.head(2))


def load_jsonl_2():
    return pd.read_json(
                        path_or_buf = f'{input_file2}train.jsonl',
                        lines=True) 
df2 = load_jsonl_2()
print(df2.head(2))

frames= [df1,df2]
resulting_df = pd.concat(frames)

print(resulting_df.head())
print(resulting_df.tail())
