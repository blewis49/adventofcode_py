from collections import defaultdict

myfile = open('./data/day4input.txt').read().split('\n')
myfile.sort()

def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])

C = defaultdict(int)
CM = defaultdict(int)
guard = None
asleep = None
for line in myfile:
    if line:
        time = parseTime(line)
        if 'begins shift' in line:
             guard = int(line.split()[3][1:])
             asleep = None
        elif 'falls asleep' in line:
             asleep = time
        elif 'wakes up' in line:
            #iterates as t goes from time asleep to time awake
            for t in range(asleep, time):
                #a dict with guard number and minute slept as key and
                #number of times each min slept as value
                CM[(guard, t)] += 1
                #a dict to count the total number of minutes each guard sleeps
                C[guard] += 1

def argmax(d):
     best = None
     for k,v in d.items():
         if best is None or v > d[best]:
             best = k  #k is the tuple (guard#, min_slept)
     return best

best_guard, best_min = argmax(CM)
sleepiest_guard = argmax(C) #needed for part 1
print(best_guard, best_min, sleepiest_guard)
print(sleepiest_guard*best_min)
