def search_bfs(maze: list, current_pivot: int, visited_points: list):
    # Pseudo code
    """_summary_

    Args:
        maze (list): _description_
        current_pivot (set): _description_
        visited_points (set): _description_
    """
    """
    new_queue
    add current_pivot to q
    mark curret_point as visited
    while q is not empty:    
    """
    goal_point: list = []
    neighbors: list = []
    q: list = []
    q.append(current_pivot)
    visited_points.append(current_pivot)
    while q:
        current_pivot = q.pop(0)
        # add available cells north, south, and west
        for neighbor in neighbors:
            if neighbor not in visited_points:
                current_pivot = neighbor
                visited_points.append(neighbor)
                q.append(neighbor)
                if neighbor is goal_point:
                    return neighbor
    return "No Path to goal"

    ...
