import os
os.environ['CUDA_VISIBLE_DEVICES'] = '5'
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
import json
import argparse
import time
parser = argparse.ArgumentParser(description="Example script for converting Txt or Jsonl file format to Parquet",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("input_path1",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path2",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path3",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("out_path", help="Location of output file dir")
args = parser.parse_args()
print(args)
config = vars(args)

input_file1  = config['input_path1']
input_file2  = config['input_path2']
input_file3  = config['input_path3']
output_dir   = config['out_path']

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

resulting_df.to_parquet(f'{output_dir}all_train.parquet') 
# Read Parquet file in python 
time.sleep(3)
# --------------------------------------------------
df_parquet = pd.read_parquet(f'{output_dir}all_train.parquet') 
print(df_parquet.head())
print(df_parquet['file_name'][10], df_parquet['text'][10])
# ---------------------------------------------------
pq_array = pa.parquet.read_table(f'{output_dir}all_train.parquet', memory_map=True)  
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")
pq_array = pa.parquet.read_table(f'{output_dir}all_train.parquet', memory_map=False) 
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")
# ---------------------------------------------------
# Inspecting the Parquet File Metadata
parquet_file = pq.ParquetFile(f'{output_dir}all_train.parquet') 
print(parquet_file)
metadata = parquet_file.metadata
print(metadata)
#---------------------------------------------------
# Converting dataframe to jsonl
time.sleep(3)
reddit = resulting_df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
with open(f"{output_dir}all_train.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
