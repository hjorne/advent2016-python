import numpy as np
import heapq as hq
from copy import deepcopy


def find_neighbors(x, y):
    neighbor_list = []
    dr = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for dx, dy in dr:
        if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y:
            neighbor_list.append((x + dx, y + dy))
    return neighbor_list


def generate_branches(avail, moves, posG):
    for x in reversed(range(max_x + 1)):
        for y in range(max_y + 1):
            neighbors = find_neighbors(x, y)
            for xn, yn in neighbors:
                # If there's data there to be moved, and if the used can fit in
                # the neighbors avail
                used = size[x, y] - avail[x, y]
                if 0 < used <= avail[xn, yn]:
                    new_avail = avail.copy()

                    new_avail[xn, yn] -= used
                    new_avail[x, y] += used
                    state = new_avail.tobytes()

                    if state not in prev_states:
                        prev_states.add(state)
                        temp = posG
                        if (x, y) == posG:
                            if (xn, yn) == (0, 0):
                                print moves + 1, 'fuuuuck'
                                exit()
                            temp = (xn, yn)

                        hq.heappush(q, (moves + 1 + sum(temp),
                                        np.random.rand(), moves + 1, new_avail,
                                        temp))

if __name__ == '__main__':
    fname = 'day22_test_input.txt'
    with open(fname) as day22_input:
        last_line = day22_input.readlines()[-1]
        split = last_line.split()
        split_pos = split[0].split('-')
        max_x = int(split_pos[1][1:])
        max_y = int(split_pos[2][1:])

    size = np.zeros((max_x + 1, max_y + 1), dtype=np.uint16)
    avail = np.zeros((max_x + 1, max_y + 1), dtype=np.uint16)
    with open(fname) as day22_input:
        day22_input.readline()
        day22_input.readline()
        for line in day22_input.readlines():
            split = line.split()
            split_pos = split[0].split('-')
            x = int(split_pos[1][1:])
            y = int(split_pos[2][1:])
            size[x, y] = int(split[1][:-1])
            avail[x, y] = int(split[3][:-1])

    # Insert part I here

    x, y = max_x, 0
    q = []
    # (Priority, # of moves, state (avail numpy array), pos of important data)
    hq.heappush(q, (x + y, np.random.rand(), 0, avail, (x, y)))
    prev_states = {avail.tostring()}
    m = set()
    while q:
        p, rand, moves, avail, pos = hq.heappop(q)
        if moves not in m:
            print moves, len(q)
            m.add(moves)
        generate_branches(avail, moves, pos)
