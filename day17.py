from hashlib import md5
from collections import deque

i_to_dirs = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
dirs_to_pos = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
open = {'b', 'c', 'd', 'e', 'f'}

passcode = 'ulqzkmiv'
paths = set()
queue = deque()
queue.append((0, 0, ''))

max_pathlen = 0
first_path = True
while queue:
    x, y, path = queue.popleft()

    md5_hash = md5(passcode + path).hexdigest()[:4]
    dirs = [i_to_dirs[i] for i, c in enumerate(md5_hash) if c in open]
    pos = [dirs_to_pos[d] for d in dirs]
    for d, (dx, dy) in zip(dirs, pos):
        if x + dx == 3 and y + dy == 3:
            if first_path:
                print 'Shortest path is: {0}'.format(path + d)
                first_path = False
            elif len(path + d) > max_pathlen:
                max_pathlen = len(path + d)
        elif 0 <= x + dx <= 3 and 0 <= y + dy <= 3:
            queue.append((x + dx, y + dy, path + d))

print 'Length of longest path is {0}'.format(max_pathlen)
