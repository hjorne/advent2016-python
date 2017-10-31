instructions = []
with open('day12_input.txt') as day12_input:
    for line in day12_input.readlines():
        instructions.append(line.strip())

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

i = 0
while i < len(instructions):
    split = instructions[i].split()
    if split[0] == 'cpy':
        if split[1].isdigit():
            registers[split[2]] = int(split[1])
        else:
            registers[split[2]] = registers[split[1]]
    elif split[0] == 'inc':
        registers[split[1]] += 1
    elif split[0] == 'dec':
        registers[split[1]] -= 1
    elif split[0] == 'jnz':
        if split[1].isdigit() and split[1] != '0' or registers[split[1]] != 0:
            # -1 to account for the fact it will get incremented below
            i += int(split[2]) - 1
    i += 1

print 'The value of register a is {0}'.format(registers['a'])
