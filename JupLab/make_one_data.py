import pandas as pd
from subprocess import call

# path = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/sample/f1/train.jsonl"
path ="/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v1/train.jsonl"
df = pd.read_json(path_or_buf=path, lines=True,)
print(df.head())
# make a duplicate dataframe
ndf = df.copy(deep=True)
for i in range(len(ndf)):
    og_fn = ndf['file_name'][i]
    new_fn = 'A_{fn}'.format(fn=og_fn)
    ndf.loc[i, ['file_name']] = [new_fn]

# create output directory
call(['mkdir lines_hu_v1_1'], shell=True)

# copy original imgs folder into out_folder
dst = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v1_1'
src = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v1/images'
cmd = 'cp -a {s} {d}'.format(s=src, d=dst)
call([cmd, src, dst], shell=True)

# write the new dataframe to '/.../out_folder/train.jsonl'
with open(f'{dst}/train.jsonl', 'w') as f:
    f.write(ndf.to_json(orient='records', lines=True))

call(['pwd'], shell=True)
cmd = 'for f in *.jpg; do mv "$f" "A_$f"; done'
call([cmd], shell=True, cwd=dst + '/images')
