# Set filename variable to store poem txt file
filename = "poem.txt"

# Defined get_file_lines function to open txt file and read line by line as list
def get_file_lines(filename):
    infile = open(filename, "r")
    read_lines = infile.readlines()
    return read_lines

# Assigned prev function as new lines_list variable to retrieve poem list within next function

lines_list = get_file_lines(filename)

# Used for loop in order for function to print reverse enumerated version of poem list
def lines_printed_backwards(lines_list):
    for line, value in reversed(list(enumerate(lines_list))):
        print(line, value)