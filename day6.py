from collections import defaultdict

""" Parts 1 and 2, because they're virtually identical"""
transmission = []
with open('day6_input.txt') as day6_input:
    for line in day6_input.readlines():
        transmission.append(line.strip())

message = ''
for i in range(len(transmission[0])):
    count = defaultdict(int)
    for j in range(len(transmission)):
        count[transmission[j][i]] += 1

    # Part 1: [-1], Part 2: [0]
    common_char = sorted(count, key=count.get)[0]
    message += common_char

print message
