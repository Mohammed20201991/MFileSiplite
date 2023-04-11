import os

folder = r"/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v2/iam/img/"
# Listing the files of a folder
print('Before rename')
files = os.listdir(folder)
print(files)

# rename each file one by one
for file_name in files:
    # construct full file path
    old_name = os.path.join(folder, file_name)

    # Changing the extension from txt to pdf
    new_name = old_name.replace('.png', '.jpg')
    os.rename(old_name, new_name)

# print new names
print('After rename')
print(os.listdir(folder))
