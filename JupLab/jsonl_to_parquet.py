# https://arrow.apache.org/docs/python/parquet.html#reading-and-writing-single-files
# https://www.youtube.com/watch?v=kYghFTfDXnU&t=10s
import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]},
                   index=list('abc'))
table = pa.Table.from_pandas(df)

pq.write_table(table, 'example.parquet')

table2 = pq.read_table('example.parquet')
print(table2)

m = table2.to_pandas()
print("m" ,m.head())
print(table2.to_pandas())

n = pq.read_table('example.parquet', columns=['one', 'three'])
print("n", type(n), n)
x = pq.read_pandas('example.parquet', columns=['two']).to_pandas()
print(x.head())


pq_array = pa.parquet.read_table("example.parquet", memory_map=True)
print("RSS: {}MB".format(pa.total_allocated_bytes() >> 20))

pq_array = pa.parquet.read_table("example.parquet", memory_map=False)
print("RSS: {}MB".format(pa.total_allocated_bytes() >> 20))

# Inspecting the Parquet File Metadata
parquet_file = pq.ParquetFile('example.parquet')
print(parquet_file)
metadata = parquet_file.metadata
print(metadata)

# ---------------------------------------------------
# if Iam reading *.txt file 
import pandas as pd
txt = False
if txt:
    df = pd.read_csv(
                      'input.txt' ,
                      header=None,
                      delimiter='   ',
                      encoding="utf8",
                      engine='python'
                      )    
    df.rename(columns={0: "file_name", 1: "text"}, inplace=True)
else: 
    df = pd.read_json(path_or_buf = "input.jsonl", lines=True)

df.to_parquet('out.parquet')
# for vitulizing results 
# https://www.parquet-viewer.com/
# for extra reading 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html
# https://gist.github.com/jiffyclub/905bf5e8bf17ec59ab8f#file-hdf_to_parquet-py
# Read Parquet file in python 
parquet_file= r"/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/out.parquet"
df =pd.read_parquet(parquet_file)
print(df.head())

# write without compression 
csv_out = r"csv_out.csv"
df.to_csv(csv_out,index=False,sep='\t')

# write with gzip comparssion
comparessed_csv= r"out.csv.gz"
df.to_csv(comparessed_csv, index=False,compression='gzip')
