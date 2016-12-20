from math import log, floor

# This is the Josephus Problem
# https://en.wikipedia.org/wiki/Josephus_problem#k.3D2
n = 3014387
print 'Elf {0} ends up with the presents'.\
    format(int(2*(n - 2**floor(log(n, 2))) + 1))

# Dynamic programming solution for part 2
W = {2: 0}
for i in range(3, n + 1):
    W[i] = (W[i-1] + 1) % (i - 1)
    W[i] += (W[i] >= i/2)
print 'Elf {0} ends up with the presents'.format(W[n] + 1)
