n = 35651584

# Easier to work with lists than strings
a = list('10111100110001111')
while len(a) < n:
    b = ['1' if c == '0' else '0' for c in reversed(a)]
    a += ['0'] + b

checksum = a[:n]
while len(checksum) % 2 == 0:
    # Splits the checksum into pairs
    checksum = [checksum[i:i + 2] for i in range(0, len(checksum), 2)]
    # For each pair, print appropriate character
    checksum = ['1' if c[0] == c[1] else '0' for c in checksum]
print ''.join(checksum)
