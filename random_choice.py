import glob, random
import pandas as pd
import shutil
import time 
import json
import os
# file_path_type = ["./Memes/*.png", "./Memes/*.jpeg"]
# ['/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/test/*.jpg']
# images = glob.glob(random.choice(file_path_type))
# random_image = random.choice(images)
source_folder      = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v1/'
destination_folder = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v2/v1/"

def load_jsonl(path):
    return pd.read_json(
                        path_or_buf = path,
                        lines=True) 
df = load_jsonl(f'{source_folder}train.jsonl')
print(df.head())
 
# n is the number of samples we wanna choose  
new_df = df.sample(n = 100000) #0000
print(len(new_df),new_df.head())
#---------------------------------------------------
# Converting new dataframe to jsonl
time.sleep(3)
reddit = new_df.to_dict(orient= "records")
print(type(reddit) , len(reddit))
# we have list of dict[{},{},{}]
with open(f"{destination_folder}100_000_sample_v1.jsonl","w") as f:
    for line in reddit:
        f.write(json.dumps(line,ensure_ascii=False) + "\n")

def make_copy(file_name):
    source = source_folder + 'images/'+ file_name
    print('source',source)
    destination = destination_folder + 'img/' + file_name 
    print('destenation', destination) 
    if os.path.isfile(source):       
        shutil.copyfile(source, destination) # CTRL + C
        print('Copied :', file_name)


# def load_jsonl2():
#     return pd.read_json(
#                         path_or_buf = f'{destination_folder}sample_v1.jsonl',
#                         lines=True) 

new_df = load_jsonl(f'{destination_folder}100_000_sample_v1.jsonl')
print(new_df.head(10))
# print(new_df['file_name'].iloc[:-1])
# print(new_df.index[-1])

# idx = new_df.index[-1]
# print(len(new_df))
for idx in range(len(new_df)):
    # print('idx',idx)
    file_name = new_df['file_name'][idx]  # come from df 
    print(file_name)
    make_copy(file_name)

# for moving single file 
# capture source file 
# original = r'df['file_name][idx]'
# capture destnation file 
# target = r'/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v3/labels.txt'
