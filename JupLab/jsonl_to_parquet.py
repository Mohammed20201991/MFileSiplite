# https://arrow.apache.org/docs/python/parquet.html#reading-and-writing-single-files
# https://www.youtube.com/watch?v=kYghFTfDXnU&t=10s
# for vitulizing results 
# https://www.parquet-viewer.com/
# for extra reading 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html
# https://gist.github.com/jiffyclub/905bf5e8bf17ec59ab8f#file-hdf_to_parquet-py
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '5'
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
import argparse

parser = argparse.ArgumentParser(description="Example script for converting Txt or Jsonl file format to Parquet",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("input_path",   help="Location of input file (single text file or Single jsonl file )")
parser.add_argument("out_path", help="Location of output file dir")
args = parser.parse_args()
print(args)
config = vars(args)

input_file  = config['input_path']
output_dir  = config['out_path']

# ---------------------------------------------------
# if Iam reading *.txt file 
txt = False # True
iam_test = True
if txt:
    df = pd.read_csv(
                      input_file,
                      header=None,
                      delimiter='   ',
                      encoding="utf8",
                      engine='python'
                      )    
    df.rename(columns={0: "file_name", 1: "text"}, inplace=True)
# if Iam reading *.jsonl file
if iam_test:    
    df = pd.read_fwf(input_file, header=None)
    df.rename(columns={0: "file_name", 1: "text"}, inplace=True)
    del df[2]
    # some file names end with jp instead of jpg, let's fix this
    df['file_name'] = df['file_name'].apply(lambda x: x + 'g' if x.endswith('jp') else x)
    # df.head()

else: 
    df = pd.read_json(path_or_buf = input_file,
                      lines=True,
                      )
# Converting dataframe to parquet 
df.to_parquet(output_dir)
# Read Parquet file in python 

# ---------------------------------------------------
df =pd.read_parquet(output_dir)
print(df.head())
print(df['file_name'][100], df['text'][100])

# ---------------------------------------------------
pq_array = pa.parquet.read_table(output_dir, memory_map=True)
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")
pq_array = pa.parquet.read_table(output_dir, memory_map=False)
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")

# ---------------------------------------------------
# Inspecting the Parquet File Metadata
parquet_file = pq.ParquetFile(output_dir)
print(parquet_file)
metadata = parquet_file.metadata
print(metadata)
