instructions = []
with open('day23_input.txt') as day23_input:
    for line in day23_input.readlines():
        instructions.append(line.strip())

registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

i = 0
while i < len(instructions):
    split = instructions[i].split()
    if split[0] == 'cpy':
        registers[split[2]] = (registers[split[1]] if split[1].isalpha()
                               else int(split[1]))
    elif split[0] == 'inc':
        registers[split[1]] += 1
    elif split[0] == 'dec':
        registers[split[1]] -= 1
    elif split[0] == 'jnz':
        x = registers[split[1]] if split[1].isalpha() else int(split[1])
        y = registers[split[2]] if split[2].isalpha() else int(split[2])
        if x != 0:
            # -1 to account for the fact it will get incremented below
            i += y - 1
    elif split[0] == 'tgl':
        j = i + registers[split[1]]
        if 0 <= j < len(instructions):
            toggle = instructions[j].split()
            if len(toggle) == 2:
                toggle[0] = 'dec' if toggle[0] == 'inc' else 'inc'
            elif len(toggle) == 3:
                toggle[0] = 'cpy' if toggle[0] == 'jnz' else 'jnz'
            instructions[j] = ' '.join(toggle)
    i += 1
print 'The value of register a is {0}'.format(registers['a'])
