from copy import copy


def generate_branches(F, E, moves, prev_states):
    """ Uses a backtracking approach. This function generates the branches in
        the tree, using prev_states to ensure branches are not visited
        multiple times
    """
    S = []
    for item_i in F[E]:
        # Generate all single-item only moves
        for dE in [-1, 1]:
            if E == 3 and dE == 1 or E == 0 and dE == -1:
                continue
            # The triple copy here may seem odd, but it's by far the fastest
            Fn = copy(F)
            Fn[E] = copy(F[E])
            Fn[E + dE] = copy(F[E + dE])
            Fn[E].remove(item_i)
            Fn[E + dE].add(item_i)
            if legal_state(Fn):
                # Only immutable objects (tuples/frozensets) are hashable
                hashable = (E + dE, tuple([frozenset(x) for x in Fn]))
                if hashable not in prev_states:
                    prev_states.add(hashable)
                    S.append((E + dE, Fn, moves + 1))
        # Generate all double-item moves
        for item_j in F[E]:
            if item_i != item_j:
                for dE in [-1, 1]:
                    if E == 3 and dE == 1 or E == 0 and dE == -1:
                        continue
                    Fn = copy(F)
                    Fn[E] = copy(F[E])
                    Fn[E + dE] = copy(F[E + dE])
                    moved = {item_i, item_j}
                    Fn[E] -= moved
                    Fn[E + dE] |= moved
                    if legal_state(Fn):
                        hashable = (E + dE, tuple([frozenset(x) for x in Fn]))
                        if hashable not in prev_states:
                            prev_states.add(hashable)
                            S.append((E + dE, Fn, moves + 1))
    return S


# Checks item_i is a generator and item_j is a chip of a different type, and
# that prefix_j + 'M' is not in the state. If all these are true, the chip is
# fried, and it's a bad state
# This can probably be done with regex but I don't know how
def legal_state(F):
    for floor in F:
        for item_i in floor:
            prefix_i = item_i[:-1]
            type_i = item_i[-1]
            if type_i == 'G':
                for item_j in floor:
                    if item_i != item_j:
                        prefix_j = item_j[:-1]
                        type_j = item_j[-1]
                        if prefix_i != prefix_j and type_j == 'M' \
                                and (prefix_j + 'G') not in floor:
                            return False
    return True

if __name__ == '__main__':
    # Example input
    F = [{'HM', 'LM'}, {'HG'}, {'LG'}, set()]

    # Part 1 input
    F = [{'PrG', 'PrM'}, {'CoG', 'CuG', 'RG', 'PlG'},
         {'CoM', 'CuM', 'RM', 'PlM'}, set()]

    # Part 2 input
    # F = [{'EG', 'EM', 'DG', 'DM', 'PrG', 'PrM'}, {'CoG', 'CuG', 'RG', 'PlG'},
    #      {'CoM', 'CuM', 'RM', 'PlM'}, set()]

    prev_states = {(0, tuple([frozenset(x) for x in F]))}
    S = generate_branches(F, 0, 0, prev_states)

    # Loops through different branches (see above in generate_branches) until
    # a solution is found. Because this is done in a BFS, this is the smallest
    # possible soution
    while S:
        E, F, moves = S.pop(0)
        if not any(F[:-1]):
            print 'Found a solution with {0} moves'.format(moves)
            break
        S += generate_branches(F, E, moves, prev_states)
