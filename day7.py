def contain_abba(strings):
    """ Checks if a list of strings contains an ABBA """
    for s in strings:
        for i in range(len(s) - 3):
            if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
                return True
    return False


""" Part 1 """
IPs = []
with open('day7_input.txt') as day7_input:
    for line in day7_input.readlines():
        # Does some minor preprocessing, since it would be duplicated below
        # Each element is a 2-tuple, one element containing all substrings
        # outside brackets, another containing all substrings inside brackets

        split = [s.split('[') for s in line.split(']')]
        last = split.pop()
        outside, inside = zip(*split)
        IPs.append((outside + tuple(last), inside))

count = 0
for outside, inside in IPs:
    outside_abba = contain_abba(outside)
    inside_abba = contain_abba(inside)
    if outside_abba and not inside_abba:
        count += 1
print '{0} IPs support TLS'.format(count)


""" Part 2 """
count = 0
for outside, inside in IPs:
    # Only done once, no need for a function this time. Finds all ABAs in
    # substrings outside brackets
    aba_list = []
    for s in outside:
        for i in range(len(s) - 2):
            if s[i] == s[i + 2] and s[i] != s[i + 1]:
                aba_list.append(s[i:i+3])

    # Converts all ABAs to BABs and looks for them in internal substrings
    ssl = False
    for aba in aba_list:
        bab = aba[1] + aba[0] + aba[1]
        for block in inside:
            if bab in block:
                ssl = True
                break
        if ssl:
            break
    if ssl:
        count += 1

print '{0} IPs support SSL'.format(count)
