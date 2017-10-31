import numpy as np

instructions = []
with open('day8_input.txt') as day8_input:
    for line in day8_input.readlines():
        instructions.append(line.strip().split())

""" Part 1 """
screen = np.zeros((6, 50))
for i in instructions:
    if i[0] == 'rect':
        m, n = map(int, i[1].split('x'))
        screen[0:n, 0:m] = 1

    elif i[1] == 'row':
        row = int(i[2][2:])
        amount = int(i[-1])
        # Roll is a convenient numpy function that does exactly what's needed
        screen[row, :] = np.roll(screen[row, :], amount)

    elif i[1] == 'column':
        col = int(i[2][2:])
        amount = int(i[-1])
        screen[:, col] = np.roll(screen[:, col], amount)

print '{0} of the pixels should be lit\n'.format(int(np.sum(screen)))


""" Part 2 """
# So the letters can be seen spatially with more ease than 0s and 1s
chararr = np.chararray((6, 50))
chararr[screen == 0] = '.'
chararr[screen == 1] = '@'

# Loops through and prints each block of 6x5 characters
for i in range(0, 50, 5):
    print chararr[:, i:i+5], '\n'
