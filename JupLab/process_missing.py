import pandas as pd
from pathlib import Path
path = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/sample/" 

df = pd.read_csv(f'{path}labels.txt',
                 header=None,
                 delimiter='   ',
                 encoding="utf8",
                 error_bad_lines=False,
                 engine='python'
                 )
df.rename(columns={0: "file_name", 1: "text"}, inplace=True)
print(df.head(11))
# print(df.tail())

# print(len(df))


def is_dir_exist(filename):
    path = "/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/sample/"
    path_to_file = f'{path}imgs/'+ filename # df['file_name'][idx] # 'readme.txt'
    path = Path(path_to_file)
    # print(path.is_file()) 
    return path.is_file() 

def drop_row(idx):
    new_df = df.drop(df.index[idx])
    return new_df 

list_fn = []
for idx in range(len(df)):
    # print(df['file_name'][idx])
    print(is_dir_exist(df['file_name'][idx]))
    if not is_dir_exist(df['file_name'][idx]):
        # new_df = drop_row(idx)
        list_fn.append(df['file_name'][idx])

for i in list_fn:
    # print(i)  
    df.drop(df[df['file_name'] == i ].index, inplace = True)
print(list_fn)
# print(new_df.head(11))
# idx = 9
# print(df.index)
# # print(df.index[idx])

print(df.head(11))

# if path.is_file():
#     print(f'The file {path_to_file} exists')
    
# else:
#     print(f'The file {path_to_file} does not exist')
#     update_df = df.drop(df.index[idx])
#     print(update_df.head(11))
