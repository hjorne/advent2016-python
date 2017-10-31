import numpy as np

""" Part 1 """
with open('day1_input.txt') as day1_input:
    input_str = day1_input.readline()
instructions = input_str.replace(' ', '').split(',')

# Heading and position are defined as vectors. Initial heading is north
heading = np.array([0, 1])
pos = np.array([0, 0])

# Rotation matrices
R = np.array([[0, -1], [1, 0]])
L = -R

for i in instructions:
    direction = i[0]
    length = int(i[1:])

    # Rotate heading vector (eval('R') will return numpy array R)
    heading = np.dot(heading, eval(direction))
    pos += length * heading

# L1 norm is just the sum of the absolute value of the components
print 'Easter Bunny HQ is {0} blocks away'.format(np.sum(abs(pos)))


""" Part 2. Reset position and heading """
heading = np.array([0, 1])
pos = np.array([0, 0])

# Keep track of every position visited in a hashset
pos_visited = set()
found = False

while not found:
    i = instructions.pop(0)
    direction = i[0]
    length = int(i[1:])
    heading = np.dot(heading, eval(direction))

    # Since each intersection encountered is a valid position, loops through
    # every step
    for step in range(length):
        pos += heading

        # numpy.array is not a hashable object, but str is, and str() is
        # injective
        pos_str = str(pos)
        if pos_str in pos_visited:
            found = True
            break
        pos_visited.add(pos_str)

print 'First location encountered twice is {0} blocks away'.\
    format(np.sum(abs(pos)))
