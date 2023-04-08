import os
os.environ['CUDA_VISIBLE_DEVICES'] = '6'
import pandas as pd
from subprocess import call
from pathlib import Path
from os import rename
import time 
# path = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/sample/f1/train.jsonl"
path ="/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/hu_words/train.jsonl"
df = pd.read_json(path_or_buf=path, lines=True,)
print(df.head())
# make a duplicate dataframe
ndf = df.copy(deep=True)
for i in range(len(ndf)):
    og_fn = ndf['file_name'][i]
    new_fn = 'words_dict_{fn}'.format(fn=og_fn)
    ndf.loc[i, ['file_name']] = [new_fn]

# create output directory
call(['mkdir hu_words_v1'], shell=True)

# copy original imgs folder into out_folder
dst = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/hu_words_v1/'
src = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/hu_words/images/'
cmd = 'cp -a {s} {d}'.format(s=src, d=dst)
call([cmd, src, dst], shell=True)

# write the new dataframe to '/.../out_folder/train.jsonl'
with open(f'{dst}train.jsonl', 'w',encoding='utf-8') as f:
    f.write(ndf.to_json(orient='records', lines=True, force_ascii=False))

call(['pwd'], shell=True)
cmd = 'for f in *.jpg; do mv "$f" "words_dict_$f"; done'
call([cmd], shell=True, cwd=f'{dst}images')

# print('renamed .. done')
# time.sleep(3)
# PATH = Path('/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v1_1/images')
# SEPARATOR = '_'
# REPEAT = 'A'

# for file in PATH.glob('*'):
#     try:
#         if len(t := file.stem.split(SEPARATOR)) > 1 and t[0] == REPEAT and t[-1].isdecimal():
#             newfile = t[0] + SEPARATOR + t[-1] + file.suffix
#             rename(file, PATH / newfile)
#     except Exception as e:
#         print(e)

# print('rename images has finshed')
# exit()
