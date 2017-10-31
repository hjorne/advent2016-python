from collections import defaultdict

""" Part 1 """
rooms = []
with open('day4_input.txt') as day4_input:
    for line in day4_input.readlines():
        rooms.append(line)

total = 0
for r in rooms:
    split = r.split('-')
    end = split.pop().strip()

    sectorID = int(end[0:3])
    checksum = list(end[4:-1])
    characters = ''.join(split)

    # Count how often each character occurs
    d = defaultdict(int)
    for c in characters:
        d[c] += 1

    # Custom comparator adhering to problem 4 specifications
    top_chars = sorted(d, cmp=lambda x, y: 1 if d[x] > d[y] else 1 if
                       d[x] == d[y] and x < y else -1, reverse=True)

    if top_chars[0:5] == checksum:
        total += sectorID
print 'The summed sector IDs is {0}'.format(total)


""" Part 2 """
for r in rooms:
    tlist = []
    split = r.split('-')
    sectorID = int(split.pop().strip()[0:3])

    tstr = ''
    for words in split:
        for c in words:
            # ASCII magic. Uses modular wrapping for O(1) execution
            ascii = (ord(c) - ord('a') + sectorID % 26) % 26 + ord('a')
            tstr += chr(ascii)
        tstr += ' '

    # Weren't given an explicit name to look for, so look for any 'north'
    if 'north' in tstr:
        print '{0} is in sector {1}'.format(tstr, sectorID)
