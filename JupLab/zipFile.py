# import required modules
import os
import zipfile
import time
# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dirName):
  # setup file paths variable
  filePaths = []
  # Read all directory, subdirectories and file lists
  for root, directories, files in os.walk(dirName):
    for filename in files:
        # Create the full filepath by using os module.
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)      
  # return all paths
  return filePaths
 
# Declare the main function
def main():
# Assign the name of the directory to zip
  dir_name = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/hu_words_v1/images/'
  out_dir = '/home/ngyongyossy/mohammad/OCR_HU_Tra2022/GPT-2_Parallel/process/hu_words_v1/'
  # Call the function to retrieve all files and folders of the assigned directory
  filePaths = retrieve_file_paths(dir_name)
  print('filePaths',len(filePaths))
  # printing the list of all files to be zipped
  print('The following list of files will be zipped:')
  time.sleep(3)
#   for fileName in filePaths:
#     print(fileName)
     
  # writing files to a zipfile
  zip_file = zipfile.ZipFile(f'{out_dir}images.zip', 'w')
  with zip_file:
    # writing each file one by one
    for file in filePaths:
      zip_file.write(file)
       
  print(f'{out_dir}images.zip file is created successfully!') 
# Call the main function
if __name__ == "__main__":
  main()
