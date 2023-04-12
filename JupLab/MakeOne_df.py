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
parser.add_argument("input_path4",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path5",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path6",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path7",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path8",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path9",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path10",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("input_path11",   help="Location of input file (single text file or Single jsonl file )")

parser.add_argument("out_path", help="Location of output file dir")
args = parser.parse_args()
print(args)
config = vars(args)

input_file1   = config['input_path1']
input_file2   = config['input_path2']
input_file3   = config['input_path3']
input_file4   = config['input_path4']
input_file5   = config['input_path5']
input_file6   = config['input_path6']
input_file7   = config['input_path7']
input_file8   = config['input_path8']
input_file9   = config['input_path9']
input_file10  = config['input_path10']
input_file11  = config['input_path11']
output_dir    = config['out_path']

def load_jsonl(path):
    return pd.read_json(
                        path_or_buf = f'{path}',# train.jsonl
                        lines=True) 

dir_   = [  input_file1,input_file2,input_file3,
            input_file4,input_file5,input_file6,
            input_file7,input_file8,input_file9,
            input_file10,input_file11,
         ]

frames = [load_jsonl(path) for path in dir_]
# for f in frames:
#     print(f.columns)
print(len(frames))
resulting_df = pd.concat(frames,ignore_index=True)
print(resulting_df.head())
print(resulting_df.tail())

resulting_df.to_parquet(f'{output_dir}all_train_v2.parquet') 
# Read Parquet file in python 
time.sleep(3)
# --------------------------------------------------
df_parquet = pd.read_parquet(f'{output_dir}all_train_v2.parquet') 
print(df_parquet.head())
print(df_parquet['file_name'][10], df_parquet['text'][10])
# ---------------------------------------------------
pq_array = pa.parquet.read_table(f'{output_dir}all_train_v2.parquet', memory_map=True)  
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")
pq_array = pa.parquet.read_table(f'{output_dir}all_train_v2.parquet', memory_map=False) 
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")
# ---------------------------------------------------
# Inspecting the Parquet File Metadata
parquet_file = pq.ParquetFile(f'{output_dir}all_train_v2.parquet') 
print(parquet_file)
metadata = parquet_file.metadata
print(metadata)
#---------------------------------------------------
# Converting dataframe to jsonl
time.sleep(3)
reddit = resulting_df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
with open(f"{output_dir}all_train_v2.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")
