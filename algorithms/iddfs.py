from core.moves import get_valid_moves, apply_move

def depth_limited_search(state, limit, visited_path, node_expanded):
    node_expanded[0] += 1

    if state.is_goal():
        return state
    
    if limit <= 0:
        return None
    
    visited_path.add(state)

    for move in get_valid_moves(state):
        neighbor = apply_move(state, move)

        if neighbor in visited_path:
            continue

        result = depth_limited_search(neighbor, limit - 1, visited_path, node_expanded)
        if result is not None:
            return result
        
    visited_path.discard(state)
    return None

def iddfs(start, max_d = 100):
    
    total_nodes = [0]  # use a list to allow modification inside depth_limited_search

    for depth in range(1, max_d + 1):
        path = set()
        result = depth_limited_search(start, depth, path, total_nodes)

        if result is not None:
            return result, total_nodes[0]
        
    return None, total_nodes[0]  # no solution found within max depth    