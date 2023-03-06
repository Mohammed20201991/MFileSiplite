import sys
import os
import shutil
sys.path.append('C:/Users/Mohammed/Downloads/data/file_sipliter/filesplit.py/New folder/MFileSiplite/')
# sys.path.append('C:/Users/Mohammed/Downloads/data/Process_HungarainCorpus/Second_siplit/MFileSiplite')
out_dir= "C:/Users/Mohammed/Downloads/data/Process_HungarainCorpus/Second_siplit/MFileSiplite/data/"
working_dir ='C:/Users/Mohammed/Downloads/data/Process_HungarainCorpus/Second_siplit/MFileSiplite/'
#  //-----------------------
# Retrieve and return output file max lines from input
def how_many_lines_per_file():
    try:
        return int(input("Max lines per output file: "))
    except ValueError:
        print("Error: Please use a valid number.")
        sys.exit(1)

#  //-----------------------
# Retrieve input filename and return file pointer
def file_dir():
    
    try:
        filename = f'{working_dir}Out_split_1.txt'  # 'G:/hu.txt/hu.txt'# 'C:/Users/Mohammed/Downloads/data/file_sipliter/filesplit.py/New folder/MFileSiplite/brown.txt' # input("Input filename: ")
        return open(filename, 'r')
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)


#  //-----------------------
# Create output file
def create_output_file_dir(num, filename):
    
    return open(f"{out_dir}split_{num}.txt", "a")  # ./data/split_{num}.txt

#  //-----------------------
# Create output directory
def create_output_directory(filename):
    output_path = f"{out_dir}" # ./data/ G:/hu.txt/data/
    try:
        if os.path.exists(output_path):  # Remove directory if exists
            shutil.rmtree(output_path)
        os.mkdir(output_path)
    except OSError:
        print("Error: Failed to create output directory.")
        sys.exit(1)

def ch_dir():
    # Print the current working directory
    print("Current working directory: {0}".format(os.getcwd()))
    # Change the current working directory
    os.chdir('./data')
    # Print the current working directory
    print("Current working directory: {0}".format(os.getcwd()))