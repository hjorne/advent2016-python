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
    # i.e. count = {a: 5, b: 2, d:10}
    count = defaultdict(int)
    for c in characters:
        count[c] += 1

    # Reverse the counting dictionary
    # i.e. inv_count = {5: [a, b, c], 1: [e], 3: [y, d]}
    inv_count = defaultdict(list)
    for k, v in count.iteritems():
        inv_count[v].append(k)

    # Go through the inv_count dictionary in order of highest occurrance, then
    # sort the characters in the list in alphabetical order
    top_chars = []
    for occ in sorted(inv_count, reverse=True):
        for c in sorted(inv_count[occ]):
            top_chars.append(c)

    # Only the first 5 characters in top_chars are relevant
    if top_chars[0:5] == checksum:
        total += sectorID
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

    # Weren't given an explicit name to look for, so just looks if 'north' is
    # a substring. Turns out, there's only 1 that matches this
    if 'north' in tstr:
        print '{0} is in sector {1}'.format(tstr, sectorID)
