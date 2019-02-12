import pandas as pd

'''Part One: read in a file of box IDs and build a checksum that
is the product of two variables where the first is the number of IDs
that contain a letter exactly two times and the other exactly three.'''

with open('./data/day2input.txt', 'r') as f:
        exactly_two = 0
        exactly_three = 0
        for line in f:
            counts = {} #build a dict to track the count of each letter in the ID
            for n in line: # build counts in this for loop
                #the counts dict looks for n in the line, returns the value and adds 1,
                #if it finds none then it returns the default value of 0
                counts[n] = counts.get(n, 0) + 1
            # now that we have the dict, check if any values occur exactly n times
            if any(v == 2 for v in counts.values()):
                    exactly_two += 1
            if any(v == 3 for v in counts.values()):
                    exactly_three += 1

        checksum = exactly_two * exactly_three
        print(checksum)

#test = pd.Series(['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab'])

'''Part Two: Search the list of box IDs to find the two that differ by exactly
one character.  Code below finds the two boxes that differ by exactly one character
but requires manual inspection to identify and remove the character that does
not match.'''

import csv
with open('./data/day2input.txt', 'r') as f:
    lines = list(csv.reader(f))
    count_diff = 0
    for i in range(len(lines)):
        for j in range(i+1,len(lines)-2):
            for x,y in zip(lines[i],lines[j]):
                for a,b in zip(x,y):
                    count_diff = sum(a!=b for a,b in zip(x,y))
                    if count_diff == 1:
                        pos = [n for n, (a,b) in enumerate(zip(x,y)) if a!=b]
                        x = x[:pos[0]] + x[(pos[0]+1):]
                        print(x)
                        break
