import shutil
import os
import time 
# for moving single file 
# capture source file 
source = r'/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v3.zip'
# capture destnation file 
destination = r'/data/aramis/ngyongyossy/Data/'

# shutil.copyfile(original, target)

# https://pynative.com/python-move-files/
# Move a Single File
shutil.move(source, destination)#copy_function = copy2
# Move All Files From A Directory

# source_folder = r""
# destination_folder = r""
# # print(os.listdir(source_folder))

# print('The data Moving has started :')
# print(f'We will Movin {len(os.listdir(source_folder))} fiels: from {source_folder}   dir')
# print(f'We Movin ... {len(os.listdir(source_folder))} fiels:')
# time.sleep(3)
# # fetch all files
# # i = 0
# for file_name in os.listdir(source_folder):
#     # construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name  # for give uinqe names  str(i) +
#     # move only files (cut)
#     if os.path.isfile(source):
#         shutil.move(source, destination) # ctrl + X
#         # shutil.copyfile(source, destination) # CTRL + C
#         print('Moved:', file_name)
#     # i = i+1
# # Move Files Matching a Pattern (Wildcard)
# # glob.glob(pathname, *, recursive=False)
time.sleep(5)
# print(f'number of fiels after Moved {len(os.listdir(destination_folder))}  fiels: to {destination_folder}   dir')
