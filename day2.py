""" Part 1 """
instructions = []
with open('day2_input.txt') as day2_input:
    for line in day2_input.readlines():
        instructions.append(line.strip())

dirs = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
x, y = 1, 1

# Transposed from the keypad in the problem to keep (x, y) indexing the same
keypad = [['1', '4', '7'],
          ['2', '5', '8'],
          ['3', '6', '9']]
combination = ''

for line in instructions:
    for c in line:
        dx, dy = dirs[c]
        # Keeps x and y in between 0 and 2
        x = min(x + dx, 2) if x > 1 else max(x + dx, 0)
        y = min(y + dy, 2) if y > 1 else max(y + dy, 0)
    combination += keypad[x][y]

print 'The combination to the first lock is: {0}'.format(combination)

keypad = [['_', '_', '5', '_', '_'],
           ['_', '2', '6', 'A', '_'],
           ['1', '3', '7', 'B', 'D'],
           ['_', '4', '8', 'C', '_'],
           ['_', '_', '9', '_', '_']]

x, y = 0, 2
combination = ''
for line in instructions:
    for c in line:
        dx, dy = dirs[c]
        x_n = min(x + dx, 4) if x > 2 else max(x + dx, 0)
        y_n = min(y + dy, 4) if y > 2 else max(y + dy, 0)

        # Ensures the same logic can be kept as before with a diamond keypad
        if keypad[x_n][y_n] != '_':
            x, y = x_n, y_n
    combination += keypad[x][y]

print 'The combination to the second lock is: {0}'.format(combination)
