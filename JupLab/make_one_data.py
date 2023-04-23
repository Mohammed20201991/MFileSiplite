import os
os.environ['CUDA_VISIBLE_DEVICES'] = '6'
import pandas as pd
from subprocess import call
from pathlib import Path
from os import rename
import time 

path ="/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/Brown/brown_en_v5/train.jsonl"
df = pd.read_json(path_or_buf=path, lines=True,)
print(df.head())
# make a duplicate dataframe
ndf = df.copy(deep=True)
for i in range(len(ndf)):
    og_fn = ndf['file_name'][i]
    new_fn = 'brown_en_v5_{fn}'.format(fn=og_fn)
    ndf.loc[i, ['file_name']] = [new_fn]

# create output directory
call(['mkdir brown_en_v5_1'], shell=True)

# copy original imgs folder into out_folder
src = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/Brown/brown_en_v5/images/'
dst = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/brown_en_v5_1/'
cmd = 'cp -a {s} {d}'.format(s=src, d=dst)
call([cmd, src, dst], shell=True)
print("copy done fro src to dst ")
# write the new dataframe to '/.../out_folder/train.jsonl'
with open(f'{dst}train.jsonl', 'w',encoding='utf-8') as f:
    f.write(ndf.to_json(orient='records', lines=True, force_ascii=False))

print("new json lines file generated ")
call(['pwd'], shell=True)
cmd = 'for f in *.jpg; do mv "$f" "brown_en_v5_$f"; done'
call([cmd], shell=True, cwd=f'{dst}')

print("done done  ")
