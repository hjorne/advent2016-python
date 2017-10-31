import heapq as hq


def find_neighbors(x, y):
    neighbor_list = []
    dr = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for dx, dy in dr:
        if (0 <= x + dx <= max_x and 0 <= y + dy <= max_y and
                (x + dx, y + dy) not in immovable):
            neighbor_list.append((x + dx, y + dy))
    return neighbor_list


def moves_to_G(E, G):
    Gprime = (G[0] - 1, G[1])
    q = []
    hq.heappush(q, (0, E))
    visited = set()
    while q:
        moves, E = hq.heappop(q)
        for n in find_neighbors(*E):
            if n == Gprime:
                return moves + 1
            if n not in visited:
                hq.heappush(q, (moves + 1, n))
                visited.add(n)
    return None

if __name__ == '__main__':
    fname = 'day22_input.txt'
    with open(fname) as day22_input:
        last_line = day22_input.readlines()[-1]
        split = last_line.split()
        split_pos = split[0].split('-')
        max_x = int(split_pos[1][1:])
        max_y = int(split_pos[2][1:])

    immovable = set()
    E = None
    with open(fname) as day22_input:
        day22_input.readline()
        day22_input.readline()
        for line in day22_input.readlines():
            split = line.split()
            split_pos = split[0].split('-')
            x = int(split_pos[1][1:])
            y = int(split_pos[2][1:])
            use = int(split[-1][:-1])
            if use > 90:
                immovable.add((x, y))
            elif use == 0:
                E = (x, y)

    m = moves_to_G(E, (max_x, 0)) + (max_x - 1) * 5 + 1
    print m

