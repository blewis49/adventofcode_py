import pandas as pd

'''Part One: read in a file of changing frequencies and
report the resulting frequency.'''

with open('./data/day1input.txt', 'r') as f:
    changes = []
    for line in f:
        line = line.rstrip()
        changes.append(line)
data = pd.Series(changes)
freq = pd.to_numeric(data)
print(freq.sum())

'''Part Two: Determine the first frequency your device reaches twice.'''
def freq_repeat(data):
    cumsum = 0
    count = 0
    freq_result = []
    while True:
        for i, val in enumerate(data):
            cumsum += val
            freq_result.append(cumsum)
            if freq_result.count(cumsum) == 2:
                return print(cumsum)
                break

#test = pd.Series([1,-2, 3, 1])
freq_repeat(freq)
