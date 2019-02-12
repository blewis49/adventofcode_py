with open('data/day5input.txt') as file:
    line = file.read().strip()

#test line = 'dabAcCaCBAcCcaDA'

def are_opp(x,y):
    return (x.lower() == y.lower()) \
    & ((x.islower() & y.isupper()) \
    | (x.isupper() & y.islower()))

def react(line):
    buf = []
    for c in line:
        if buf and are_opp(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)

agents = set([c.lower() for c in line])

#part 1
#print(react(line))

#part 2
print(min([react(line.replace(a, '').replace(a.upper(), '')) for a in agents]))
