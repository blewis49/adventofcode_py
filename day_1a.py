import pandas as pd

myfile = open('./data/day1input.txt').read().split('\n')
data = pd.Series(myfile)
print(pd.to_numeric(data).sum())
