import pandas as pd
import json
import argparse
parser = argparse.ArgumentParser(description="Example script for converting Txt or Jsonl file format to Parquet",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("input_path1",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path2",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path3",   help="Location of input file (single text file or Single jsonl file )")
args = parser.parse_args()
print(args)
config = vars(args)

input_file1  = config['input_path1']
input_file2  = config['input_path2']
input_file3  = config['input_path3']

def load_jsonl(path):
    return pd.read_json(
                        path_or_buf = f'{path}train.jsonl',
                        lines=True) 

dir_   = [input_file1,input_file2,input_file3]
frames = [load_jsonl(path) for path in dir_]

print(len(frames))
resulting_df = pd.concat(frames)
print(resulting_df.head())
print(resulting_df.tail())
