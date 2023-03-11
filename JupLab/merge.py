import pandas as pd
import os

df = pd.DataFrame(columns=['file_name', 'text'])
working_dir= "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/sample/"
# Traverse the directory recursively
for root, dirs, files in os.walk(working_dir):
    for file in files:
        if file == 'train.jsonl':
            df_temp = pd.read_json(os.path.join(root, file), lines=True)
            # print(os.path.join(root, 'imgs', df_temp['file_name']))
            # print(df_temp['file_name'].astype(str))
            df_temp['file_name'] = os.path.join(root, 'imgs', df_temp['file_name'].astype(str))
            df = df.append(df_temp, ignore_index=True)
print(df)
