#!/usr/bin/env python3
# Author ID: cfederici

f = open('data.txt', 'r')
read_data = f.read()
readlines = f.readlines()


def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    return(read_data)
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open('data.txt', 'r')
    list_of_lines = []
    for line in f:
        strip = line.strip('\n')
        list_of_lines.append(strip)
    return list_of_lines
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))