# Set filename variable to store poem txt file
filename = "poem.txt"

# Defined get_file_lines function to open txt file and read line by line as list
def get_file_lines(filename):
    infile = open(filename, "r")
    read_lines = infile.readlines()
    return read_lines

print(get_file_lines(filename))

# Assigned prev function as new lines_list variable to retrieve poem list within next function

lines_list = get_file_lines(filename)

# Used for loop in order for function to print reverse enumerated version of poem list
def lines_printed_backwards(lines_list):
    for line, value in reversed(list(enumerate(lines_list))):
        print(line, value, end=" ")

lines_printed_backwards(lines_list)

# Imported choice function from random module

from random import choice

# Again, using a for loop to print poem list in random order
# Utilized the len function to indicate the length of the poem for Python to iterate over
def lines_printed_random(lines_list):
    for i in range(len(lines_list)):
        randomline = choice(lines_list)
        print(randomline, end=" ")

lines_printed_random(lines_list)

# For the last step, I'm printing the poem with a heart symbol in front of each line starting from the top
# I'm also separating the hearts with a "~" symbol, for further aesthetic purposes
# Removed spaces between lines to match previous step outputs
def lines_printed_custom(lines_list):
      for line in lines_list:
          print("♥", line, sep=" ~ ", end=" ")

lines_printed_custom(lines_list)