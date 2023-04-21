# https://arrow.apache.org/docs/python/parquet.html#reading-and-writing-single-files
# https://www.youtube.com/watch?v=kYghFTfDXnU&t=10s
# for vitulizing results 
# https://www.parquet-viewer.com/
# for extra reading 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html
# https://gist.github.com/jiffyclub/905bf5e8bf17ec59ab8f#file-hdf_to_parquet-py
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
import argparse , json , time

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
# if I am reading *.txt file 
txt      = False 
iam_test = False
if txt:
    df = pd.read_csv(
                      input_file,
                      header=None,
                      delimiter='   ',  
                      encoding="utf8",
                      engine='python',
                    #   quotechar='"',
                      error_bad_lines=False,
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
print(df.head())
print(df['file_name'][1], df['text'][1])
# Converting dataframe to parquet 
df.to_parquet(f'{output_dir}labels.parquet') 
# Read Parquet file in python 
time.sleep(3)
# ---------------------------------------------------
df_parquet = pd.read_parquet(f'{output_dir}labels.parquet') 
print(df_parquet.head())
print(df_parquet['file_name'][10], df_parquet['text'][10])
# ---------------------------------------------------
pq_array = pa.parquet.read_table(f'{output_dir}labels.parquet', memory_map=True)  
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")
pq_array = pa.parquet.read_table(f'{output_dir}labels.parquet', memory_map=False) 
print(f"RSS: {pa.total_allocated_bytes() >> 20}MB")
# ---------------------------------------------------
# Inspecting the Parquet File Metadata
parquet_file = pq.ParquetFile(f'{output_dir}labels.parquet') 
print(parquet_file)
metadata = parquet_file.metadata
print(metadata)
#---------------------------------------------------
# Converting dataframe to jsonl
# time.sleep(3)
# reddit = df.to_dict(orient= "records")
# print(type(reddit) , len(reddit))
# # we have list of dict[{},{},{}]
# with open(f"{output_dir}train.jsonl","w") as f:
#     for line in reddit:
#         f.write(json.dumps(line,ensure_ascii=False) + "\n")
