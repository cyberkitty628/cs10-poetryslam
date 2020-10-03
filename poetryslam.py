# Set filename variable to store poem txt file
filename = "poem.txt"

# Defined get_file_lines function to open txt file and read line by line as list
def get_file_lines(filename):
    infile = open(filename, "r")
    read_lines = infile.readlines()
    return read_lines