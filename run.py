import fun

#  //-----------------------
def split_file():
    try:
        line_count  = 0 
        split_count = 1 

        max_lines = fun.how_many_lines_per_file()

        # ch_dir()
        input_file  = fun.file_dir()
        input_lines = input_file.readlines()

        fun.create_output_directory(input_file.name)
        output_file = fun.create_output_file_dir(split_count, input_file.name)

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
                    output_file = fun.create_output_file_dir(split_count, input_file.name)

    # Handle errors
    except Exception as e:
        print(f"An unknown error occurred: {e}")

    # Success message
    else:
        print(f"Successfully split {input_file.name} into {split_count} output files!")


#  //-----------------------
if __name__ == "__main__":
    split_file()
