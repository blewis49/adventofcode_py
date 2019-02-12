'''Part One:  The *build_init_matrix()* function returns a m x n zero matrix.
The argument <file> is a list of 2-element lists. It concatenates
the two string elements in each list into one string.  The function parses characters
from the string to determine the necessary dimensions to build the initial matrix.'''

'''Setup'''
import pandas as pd
import numpy as np
import re
import csv

def build_init_matrix(file): # file arg is a list of strings
    init_row_size = []
    init_col_size = []
    for str in file: #must concatenate the two elements into one string
        new_str = str[0]+','+str[1]
        regex = re.compile(r'[#@:x]')
        a = regex.sub(',',new_str).split(',')
        a = a[1:]
        init_row_size.append(int(a[2])+int(a[3]))
        init_col_size.append(int(a[1])+int(a[4]))
        max_rows = max(init_row_size)+1
        max_cols = max(init_col_size)+1
    arr = np.zeros((max_rows,max_cols))
    return arr

'''Main body'''
with open('./data/day3input.txt', 'r') as f:
    lines = list(csv.reader(f))
    arr = build_init_matrix(lines) # invokes function with a list as param

    for str in lines:
        new_str = str[0]+','+str[1]
        regex = re.compile(r'[#@:x]')
        a = regex.sub(',',new_str).split(',')
        a = a[1:]
        row_left = int(a[1])
        row_right = int(a[1]) + int(a[3])
        col_left = int(a[2])
        col_right = int(a[2]) + int(a[4])
        arr[row_left:row_right, col_left:col_right] += 1
        overlap = np.count_nonzero(arr[:] > 1)
    print('{0} square inches of total overlapped fabric.'.format(overlap))
