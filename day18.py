n = 400

# Adds safe vals on either end for ease of computation, ignores when counting
with open('day18_input.txt') as day18_input:
    rows = ['.' + day18_input.readline().strip() + '.']

# Much easier to work with bools than chars (True = '.' False = '^')
rows[0] = [c == '.' for c in rows[0]]
for i in range(n - 1):
    new_row = [True] * len(rows[i])
    for j in range(1, len(rows[i]) - 1):
        # Straightforward implementation of restrictions in problem description
        if (not rows[i][j-1] and not rows[i][j] and rows[i][j+1] or
                not rows[i][j] and not rows[i][j+1] and rows[i][j-1] or
                not rows[i][j-1] and rows[i][j] and rows[i][j+1] or
                not rows[i][j+1] and rows[i][j] and rows[i][j-1]):
            new_row[j] = False
    rows.append(new_row)

# True == 1, False == 0
print sum((sum(r[1:-1]) for r in rows))
