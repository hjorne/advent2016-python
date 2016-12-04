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
    count = defaultdict(int)
    for c in characters:
        count[c] += 1

    # Invert the counting dictionary
    inv_count = defaultdict(list)
    for k, v in count.iteritems():
        inv_count[v].append(k)

    # Go through in order of highest occurrance, then alphabetical order
    top_chars = []
    for occ in sorted(inv_count, reverse=True):
        for c in sorted(inv_count[occ]):
            top_chars.append(c)

    total += sectorID * (top_chars[0:5] == checksum)
print 'The summed sector IDs is {0}'.format(total)


""" Part 2 """
for r in rooms:
    tlist = []
    split = r.split('-')
    sectorID = int(split.pop().strip()[0:3])

    for words in split:
        tword = ''
        for c in words:
            # ASCII magic. Uses modular wrapping for O(1) execution
            ascii = (ord(c) - ord('a') + sectorID % 26) % 26 + ord('a')
            tword += chr(ascii)
        tlist.append(tword)

    tstr = ' '.join(tlist)

    # Weren't given an explicit name to look for, so look for any 'north'
    if 'north' in tstr:
        print '{0} is in sector {1}'.format(tstr, sectorID)
