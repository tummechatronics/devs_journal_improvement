




def search_bfs(maze: list, current_pivot: tuple[int, int], visited_points: list):
    # Pseudo code
    """_summary_

    Args:
        maze (list): _description_
        current_pivot (tuple): _description_
        visited_points (tuple): _description_
    """
    """
    new_queue
    add current_pivot to q
    mark current_point as visited
    while q is not empty:    
    """
    goal_point: list = []
    q: list = []
    q.append(current_pivot)
    visited_points.append(current_pivot)
    while q:
        current_pivot = q.pop(0)
        # add available cells north, south, and west
        # INFO: movement means then north,south +-1 in y direction respectively west and east means +-1 in x direction.
        # The person can't leave the maze -> no point can be negative
        neighbors = _get_neighbors(current_pivot, ...)
        for neighbor in neighbors:
            if neighbor not in visited_points:
                current_pivot = neighbor
                visited_points.append(neighbor)
                q.append(neighbor)
                if neighbor is goal_point:
                    return neighbor
    return "No Path to goal"


def _get_neighbors(current_pivot: tuple[int, int], roadblocks: list[tuple[int, int]] = None) -> list[int]:
    neighbors: list[int] = None

    for x, y in current_pivot:
        if x | y <= 0:
            
            # INFO: no movement either to left or to the right
            ...

    return neighbors
