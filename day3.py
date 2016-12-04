import numpy as np

""" Part 1 """
tri = []
count = 0
with open('day3_input.txt') as day3_input:
    for line in day3_input.readlines():
        tri.append(map(int, line.split()))

# Saving for later, since tri array gets obliterated
np_tri = np.array(tri)

for sides in tri:
    h = max(sides)
    sides.remove(h)
    if sum(sides) > h:
        count += 1

print '{0} row triangles are valid'.format(count)


""" Part 2 """
m, n = np_tri.shape
count = 0

for i in range(n):
    # Slicing the numpy array along cols instead of default rows
    l = np_tri[:, i]
    for j in range(0, m, 3):
        sides = [l[j], l[j + 1], l[j + 2]]
        h = max(sides)
        sides.remove(h)
        if sum(sides) > h:
            count += 1

print '{0} column triangles are valid'.format(count)
