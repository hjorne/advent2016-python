def maze(x, y):
    """ Just treats the maze like a 2D array of T/Fs and generates on the fly
    """
    val = x * x + 3 * x + 2 * x * y + y + y * y
    binary = map(int, list('{0:b}'.format(val + seed)))
    s = reduce(lambda x, y: x + y, binary)
    return s % 2 == 0

seed = 1352
visited = {(1, 1)}
x, y, steps = 1, 1, 0
queue = [(x, y, 0)]
num_pos = -1

# Does BFS to find way through maze.
while queue:
    x, y, steps = queue.pop(0)
    if x == 31 and y == 39:
        print 'Found (31, 39) in {0} steps'.format(steps)
    if steps <= 50:
        num_pos += 1
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if abs(dx) + abs(dy) == 1 and x + dx >= 0 and y + dy >= 0:
                if maze(x + dx, y + dy) and (x + dx, y + dy) not in visited:
                    queue.append((x + dx, y + dy, steps + 1))
                    visited.add((x + dx, y + dy))

print '{0} places are visitable in 50 steps or less'.format(num_pos)
