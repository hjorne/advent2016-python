discs = []
with open('day15_input.txt') as day15_input:
    for line in day15_input.readlines():
        d = dict()
        split = line.split()
        d['i'] = int(split[1][-1])
        d['pos'] = int(split[3])
        d['t0'] = int(float(split[-1]))
        discs.append(d)

# Uncomment for part 2
# discs.append({'i': 7, 'pos': 11, 't0': 0})

t = 0
aligned = [False] * len(discs)
while not all(aligned):
    # Looks at alignment for all the discs at once using list compressions
    aligned = [(d['t0'] + t + d['i']) % d['pos'] == 0 for d in discs]
    t += 1
print t - 1
