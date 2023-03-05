import shutil
import os

# for moving single file 
# capture source file 
# original = r'/home/ngyongyossy/mohammad/trdghm/TextRecognitionDataGeneratorHuMu23/trdg/out/hu/lines/3/labels.txt'
# # capture destnation file 
# target = r'/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v3/labels.txt'

# shutil.copyfile(original, target)

# https://pynative.com/python-move-files/
# Move a Single File
# shutil.move(source, destination, copy_function = copy2)
# Move All Files From A Directory

# source_folder = r"/home/ngyongyossy/mohammad/trdghm/TextRecognitionDataGeneratorHuMu23/trdg/out/hu/lines/3/"
source_folder = r"/home/ngyongyossy/mohammad/trdghm/TextRecognitionDataGeneratorHuMu23/trdg/out/lines/hu/"
# destination_folder = r"/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v3/images/"
destination_folder = r"/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/lines_hu_v1/images/"

# print(os.listdir(source_folder))
# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        # print('Moved:', file_name)

# Move Files Matching a Pattern (Wildcard)
# glob.glob(pathname, *, recursive=False)
