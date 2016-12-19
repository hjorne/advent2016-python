from collections import defaultdict


def trade(b):
    """ Done recursively because if one bot fills another bot with a 2nd chip,
        then that bot needs to trade. Recursion was simplest
    """
    b_low, b_high = pending.pop(b)
    chips = bots.pop(b)
    low_c, high_c = min(chips), max(chips)

    # This is what we're really looking for
    if low_c == 17 and high_c == 61:
        print 'Bot {0} compares chips 17 and 61'.format(b)
    for bot, chip in zip([b_low, b_high], [low_c, high_c]):
        if bot[0] == 'bot':
            bots[bot[1]].append(chip)
            if len(bots[bot[1]]) == 2 and bot[1] in pending:
                trade(bot[1])
        elif bot[0] == 'output':
            bins[bot[1]].append(chip)


instructions = []
with open('day10_input.txt') as day10_input:
    for line in day10_input.readlines():
        instructions.append(line.strip())

bots = defaultdict(list)
bins = defaultdict(list)
pending = dict()
for idx, i in enumerate(instructions):
    split = i.split()
    if split[0] == 'bot':
        b = split[1]
        l = split[5:7]
        h = split[-2:]
        pending[b] = (l, h)
    elif split[0] == 'value':
        v = int(split[1])
        b = split[-1]
        bots[b].append(v)

    # Put outside if-else statement to accomodate bots who have two chips but
    # had no trades posted at the time
    if len(bots[b]) == 2 and b in pending:
        trade(b)

print 'Product sum of the first 3 bins is {0}'.\
    format(bins['0'][0] * bins['1'][0] * bins['2'][0])
