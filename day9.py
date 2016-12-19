def unroll(s):
    if not ('(' in s or ')' in s):
        return len(s)
    else:
        i = s.find('(')
        l = i
        while True:
            j = s[i:].find(')') + i + 1
            length, n = map(int, s[i + 1:j - 1].split('x'))
            repeat = s[j:j + length]

            # Line for part 1
            # l += n * len(repeat)

            # Line for part 2
            l += n * unroll(repeat)

            it = s[j + length:].find('(')

            # If no more parens are found, .find() returns -1. End of problem
            if it == -1:
                return l
            i = j + length + it

            # To account for stand-alone characters in things like (2x2)AAA
            l += i - (j + length)

with open('day9_input.txt') as day9_input:
    print unroll(day9_input.readline().strip())




