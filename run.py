import sys
import os
import shutil

#  //-----------------------
def split_file():
    try:
        line_count  = 0 
        split_count = 1 

        max_lines = how_many_lines_per_file()

        # ch_dir()
        input_file  = file_dir()
        input_lines = input_file.readlines()

        create_output_directory(input_file.name)
        output_file = create_output_file_dir(split_count, input_file.name)

        for line in input_lines:

            output_file.write(line)
            line_count += 1

            # Create new output file if current output file's line count is greater than max line count
            if line_count > max_lines:
                split_count += 1
                line_count = 0

                output_file.close()

                # Prevent creation of an empty file after splitting is finished
                if not len(input_lines) == max_lines:
                    output_file = create_output_file_dir(split_count, input_file.name)

    # Handle errors
    except Exception as e:
        print(f"An unknown error occurred: {e}")

    # Success message
    else:
        print(f"Successfully split {input_file.name} into {split_count} output files!")

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

#  //-----------------------
if __name__ == "__main__":
    split_file()
