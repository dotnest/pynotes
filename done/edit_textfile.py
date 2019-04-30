# Insert a string after a word in a specific line of a text file

"""

Input file
line 1: value1
line 2: value2
line 3: value3
line 4: value4
line 5: value5

Insert, for example, "NAME" in the line number 3 just after "line" so
the file would become:

Output file
line 1: value1
line 2: value2
line NAME 3: value3
line 4: value4
line 5: value5

"""

import os

def insert_string(in_file, line, insertion):
    """ Return a list of lines after inserting a word in a specific line. """

    # your code here
    line = line - 1
    output = in_file
    lines = []
    while in_file.find('\n') != -1:
        lines.append(in_file[:in_file.find('\n')])
        in_file = in_file[in_file.find('\n')+1:]
    lines[line] = lines[line].replace('line', 'line ' + insertion)
    return lines

def write_to(outfile, from_infile):
    """ Write to a new file lines returned by the above function """

    # your code here
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/' + from_infile) as f:
        readdata = f.read()
    with open(dir_path + '/' + outfile, 'r+') as f:
        writedata = insert_string(readdata, 3, "haha ok")
        f.write('\n'.join(writedata))

write_to("outputfile", "textfile")
