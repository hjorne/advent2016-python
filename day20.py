blocked = []
with open('day20_input.txt') as day20_input:
    for line in day20_input.readlines():
        blocked.append(tuple(map(int, line.split('-'))))

blocked.sort()
overlap = True

# Loops over the data, merging any overlaps until none are found, then it knows
# it will do one last pass over the completely merged data before exiting, so
# it calculates the remaining IPs there
while overlap:
    overlap = False
    n = 4294967295 + 1
    for i, (l1, h1) in enumerate(blocked):
        n -= h1 - l1 + 1
        for j, (l2, h2) in enumerate(blocked):
            if i < j and max(l1, l2) <= min(h1, h2) or h1 + 1 == l2:
                overlap = True
                blocked.pop(j)
                blocked[i] = (min(l1, l2), max(h1, h2))
                break
        if overlap:
            break

print 'The first available IP is {0}'.format(blocked[0][1] + 1)
print 'There are {0} available IPs'.format(n)
