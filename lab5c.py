#!/usr/bin/env python3
# Author ID: cfederici

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        add = int(number1) + int(number2)
        return(add)
    except ValueError:
        return('error: could not add numbers')

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        list_of_lines = []
        for line in f:
            strip = line.strip() + ('\n')
            list_of_lines.append(strip)
        return(list_of_lines)
    except FileNotFoundError:
        return('error: could not read file')
    


if __name__ == '__main__':
    print(add(10,5))
    print(add('10',5))
    print(add('abc',5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))