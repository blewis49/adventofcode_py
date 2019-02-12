import pandas as pd

with open('./data/day4input.txt') as file:
    dict = {}
    sleep_time=0

    head = file.readlines()
    head.sort()
    for i, f in enumerate(head):
        line = f.split()

        if 'Guard' in line:
            guard = line[3]
        elif 'falls' in line:
            start_sleep = int(line[1][-3:-1])

        elif 'wakes' in line:
            sleep_time = list(range(start_sleep, int(line[1][-3:-1])))

            if guard in dict.keys():
                dict[guard] += sleep_time

            else:
                dict[guard] = sleep_time

    # The guard who sleeps the most (longest list of numbers)
    max_sleep = max(dict, key= lambda x: len(dict[x]))
    guard_num = int(max_sleep[1:])
    minutes_slept = dict[max_sleep]

    counts={}
    for m in minutes_slept:
        counts[m] = counts.get(m, 0) + 1
    max_value = max(counts.values())
    max_minute = [k for k, v in counts.items() if v == max_value]

    print('Guard#', guard_num)
    print('The max time a minute was slept was {}'.format(max_value))
    print('The minute slept most often was {}'.format(max_minute))
    print(guard_num * int(max_minute[0]))
