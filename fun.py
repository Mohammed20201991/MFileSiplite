import sys
import os
import shutil
sys.path.append('C:/Users/Mohammed/Downloads/data/file_sipliter/filesplit.py/New folder/MFileSiplite/')
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
        filename = input("Input filename: ")
        return open(filename, 'r')
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)


#  //-----------------------
# Create output file
def create_output_file_dir(num, filename):
    return open(f"./data/output_{filename}/split_{num}.txt", "a")


#  //-----------------------
# Create output directory
def create_output_directory(filename):
    output_path = f"./data/output_{filename}"
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