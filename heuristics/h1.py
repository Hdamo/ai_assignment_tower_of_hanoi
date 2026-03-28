def h1(state):
    count = 0
    for p in state.pegs:
        if p != 'C':
            count += 1
    return count        