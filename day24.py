from collections import defaultdict
from itertools import permutations


def find_neighbors(x, y):
    neighbor_list = []
    dr = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for dx, dy in dr:
        xn, yn = x + dx, y + dy
        if ((xn, yn) not in visited and grid[xn][yn] != '#'
                and 0 <= xn <= max_x and 0 <= yn <= max_y):
            visited.add((xn, yn))
            neighbor_list.append((xn, yn))
    return neighbor_list

grid = []
locs = {}
with open('day24_input.txt') as day24_input:
    for i, line in enumerate(day24_input.readlines()):
        for j, c in enumerate(line):
            if c.isdigit():
                locs[int(c)] = (i, j)
        grid.append(line)
max_x = len(grid) - 1
max_y = len(grid[0]) - 1

dists = defaultdict(dict)
for node, (x, y) in locs.iteritems():
    visited = {(x, y)}
    q = [(1, x, y) for (x, y) in find_neighbors(x, y)]
    while q:
        m, x, y = q.pop(0)
        if grid[x][y].isdigit():
            found = int(grid[x][y])
            if found not in dists[node]:
                dists[node][found] = m
        q += [(m + 1, x, y) for (x, y) in find_neighbors(x, y)]

min_pathlen = max(dists[0].values()) * (len(dists) + 1)
for order in permutations(range(1, len(locs))):
    order = [0] + list(order) + [0]
    split = [order[i:i + 2] for i in range(len(order) - 1)]
    pathlen = sum(map(lambda x: dists[x[0]][x[1]], split))
    if pathlen < min_pathlen:
        min_pathlen = pathlen
print min_pathlen
