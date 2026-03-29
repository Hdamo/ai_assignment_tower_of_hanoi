from core.moves import get_valid_moves, apply_move

def dastar(state, g, threshhold, heuristic, current_path, counter):

    counter[0] += 1
    f = g + heuristic(state)

    if f > threshhold:
        return f, None
    
    if state.is_goal():
        return f, state
    
    next_threshhold = float('inf')
    current_path.add(state)

    for move in get_valid_moves(state):
        neighbor = apply_move(state,  move)

        if neighbor in current_path:
            continue    

        t, found = dastar(neighbor, g + 1, threshhold, heuristic, current_path, counter)

        if found is not None:
            return t, found
        
        if t < next_threshhold:
            next_threshhold = t

    current_path.discard(state)
    return next_threshhold, None


def idastar(start, heuristic):

    threshhold = heuristic(start)
    total_nodes = [0]

    while True:
        path = set()
        t, goal = dastar(start, 0, threshhold, heuristic, path, total_nodes)

        if goal is not None:
            return goal, total_nodes[0]
        
        if t == float('inf'):
            return None, total_nodes[0]  # no solution
        
        threshhold = t