def react(list):
    for i, (x,y) in enumerate(zip(list[::],list[1::])):
        if x.lower() == y.lower():  # are chars equal?
            # do they react?
            if (x in list) & ((x.islower() & y.isupper()) | (x.isupper() & y.islower())):
                list.pop(i)  #remove elements from a list
                list.pop(i)
                return list


def chk_react(list):
    check=0
    for x,y in zip(list[::],list[1::]):
        if x.lower() == y.lower():  # are chars equal?
            # do they react?
            if (x.islower() & y.isupper()) | (x.isupper() & y.islower()):
                check += 1
                return check

    return check


with open('data/day5input.txt') as file:
    f = file.read().splitlines()[0]
    my_list = [c for c in f if c is not None]

    while chk_react(my_list) > 0:
        my_list = react(my_list)

    print('The number of units remaining is {}'.format(len(my_list)))
