#Open a text file and read the first N line.
#head is a list with each element in the list as a string
import pandas as pd
import numpy as np
import re
import csv
from datetime import datetime

def test_fun(s):
    d = {}
    sleep_time = []
    for i in s:
        count = 0
        if i[1][0] == 'Guard':
            d['guard'] = i[1][1]
            print(d)
        if i[1][0] != 'Guard':
            count += 1
            print(count)
            if i[1][0] == 'falls':
                sleep_time.append(i[0] - i[0])
                print(sleep_time)
    return d

with open('./data/day4input.txt', 'r') as f:
    head = f.readlines()[0:10]
    #myfile = open('./data/day4input.txt').read().split('\n')
    lst=[]
    for str in head:
        l = re.split(r'[\[\]]',str)
        l = l[1:]
        l[0] = datetime.strptime(l[0], '%Y-%m-%d %H:%M')
        l[1] = re.split(r'\s', l[1])
        lst.append(list((l[0], l[1][1:3])))
    s = pd.Series(lst).sort_values()
    test_fun(s)
    #print(s)
