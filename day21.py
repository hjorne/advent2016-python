def rotate(l, n):
    n %= len(l)
    return l[-n:] + l[:-n]

instructions = []
with open('day21_input.txt') as day21_input:
    for line in day21_input.readlines():
        instructions.append(line.strip().split())
orig = []
new = []
s = list('abcdefgh')
for instr in instructions:
    if instr[0] == 'swap':
        if instr[1] == 'position':
            i, j = int(instr[2]), int(instr[-1])
            s[i], s[j] = s[j], s[i]
        elif instr[1] == 'letter':
            i = s.index(instr[2])
            j = s.index(instr[-1])
            s[i], s[j] = s[j], s[i]
    elif instr[0] == 'move':
        i, j = int(instr[2]), int(instr[-1])
        c = s.pop(i)
        s.insert(j, c)
    elif instr[0] == 'rotate':
        if instr[1] == 'based':
            i = s.index(instr[-1])
            n = 1 + i + (i >= 4)
            s = rotate(s, n)
        else:
            n = int(instr[2])
            if instr[1] == 'left':
                s = rotate(s, -n)
            elif instr[1] == 'right':
                s = rotate(s, n)
    elif instr[0] == 'reverse':
        i, j = int(instr[2]), int(instr[-1])
        s[i:j+1] = s[i:j+1][::-1]
print ''.join(s)


s = list('fbgdceah')
new.append(''.join(s))
for idx, instr in enumerate(reversed(instructions)):
    if instr[0] == 'swap':
        if instr[1] == 'position':
            i, j = int(instr[2]), int(instr[-1])
            s[i], s[j] = s[j], s[i]
        elif instr[1] == 'letter':
            i = s.index(instr[2])
            j = s.index(instr[-1])
            s[i], s[j] = s[j], s[i]

    elif instr[0] == 'move':
        i, j = int(instr[2]), int(instr[-1])
        i, j = j, i
        c = s.pop(i)
        s.insert(j, c)

    elif instr[0] == 'rotate':
        if instr[1] == 'based':
            i = s.index(instr[-1])
            if i == 0:
                j = ((i - 1) / 2) % len(s)
                s = rotate(s, abs(j - i))
            elif i % 2 == 0:
                j = (i - 2 + len(s)) / 2
                s = rotate(s, abs(j - i))
            else:
                j = (i - 1) / 2
                s = rotate(s, -abs(j - i))
        else:
            n = int(instr[2])
            if instr[1] == 'left':
                s = rotate(s, n)
            elif instr[1] == 'right':
                s = rotate(s, -n)

    elif instr[0] == 'reverse':
        i, j = int(instr[2]), int(instr[-1])
        s[i:j+1] = s[i:j+1][::-1]

print ''.join(s)