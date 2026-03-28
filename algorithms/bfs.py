from collections import deque
from core.moves import get_valid_moves, apply_move

def bfs(start):
    queue = deque()
    queue.append(start)
    explored = {start}

    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current.is_goal():
            return current, nodes_expanded
        
        for move in get_valid_moves(current):
            neighbor = apply_move(current, move)

            if neighbor not in explored:
                explored.add(neighbor)
                queue.append(neighbor)

    return None, nodes_expanded  # no solution found            