#
# ? I should move _check_point_inside_grid and _get_neighbors to the maze
import numpy as np


def _check_point_inside_grid(point, grid_boundaries) -> bool:
    """Check if a point is inside a rectangular grid boundary."""
    x_min = min(p[0] for p in grid_boundaries)
    x_max = max(p[0] for p in grid_boundaries)
    y_min = min(p[1] for p in grid_boundaries)
    y_max = max(p[1] for p in grid_boundaries)

    x, y = point

    return True if x_min <= x <= x_max and y_min <= y <= y_max else False


def _move_cost(point_origin, target_point):
    return 5 if target_point[1] > point_origin[1] or target_point[1] < point_origin[1] else 1


def _calculate_cost(point_origin, target_point) -> np.float64:
    distance_to_root = np.linalg.norm(np.array(point_origin) - np.array(target_point))
    cost_to_move = _move_cost(point_origin, target_point)
    return distance_to_root + cost_to_move

    ...


def _get_neighbors(current_pivot: tuple[int, int], roadblocks: list[tuple[int, int]], boundaries) -> list[int]:
    neighbors: list[tuple[int, int]] = []
    # TODO: refactor this basic set of movements.
    movement_directions: list[tuple[int, int]] = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for move_direction in movement_directions:
        # * move to the north then to the south then to the west and then to the east
        temp_point = tuple(
            [x_component + y_component for x_component, y_component in zip(current_pivot, move_direction)]
        )
        if temp_point in roadblocks or not _check_point_inside_grid(temp_point, boundaries):
            continue

        neighbors.append(temp_point)
    return neighbors


def search_bfs(maze: list, current_pivot: tuple[int, int], visited_points: list) -> list[tuple[int, int]]:
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
    # * INFO: this is actually something that shouldn't be part of the algorithm. but part of the maze creation:
    goal_point, roadblocks, boundaries = maze

    q: list = []
    q.append(current_pivot)
    visited_points.append(current_pivot)
    attempt = 0
    while q:
        current_pivot = q.pop(0)
        neighbors = _get_neighbors(current_pivot, roadblocks, boundaries)
        for neighbor in neighbors:
            if neighbor not in visited_points:
                visited_points.append(neighbor)
                q.append(neighbor)
                #! Just for documentation
                # _, fig = plot_maze(maze_dim_x, maze_dim_y, neighbor, goal_point, roadblocks)
                # fig.savefig(f"{attempt}_{visited_points}.png")
                if neighbor == goal_point:
                    return visited_points
                attempt += 1
    print(f"Path to {goal_point} not found ")
    return visited_points


def search_dfs(maze: list, root_point: tuple[int, int], visited_points: list) -> list[tuple[int, int]]:
    stack: list = []
    stack.append(root_point)
    goal_point, roadblocks, boundaries = maze
    attempt_stack: list = []
    parent_map = {}  # Dictionary to store parent relationships

    while stack:
        current_point = stack.pop()
        attempt_stack.append(current_point)
        if current_point not in visited_points:
            visited_points.append(current_point)
            if current_point == goal_point:
                print(parent_map)  # Store parent reference
                return visited_points, attempt_stack
            else:
                neighbors = _get_neighbors(current_point, roadblocks, boundaries)
                for neighbor in neighbors:
                    parent_map[neighbor] = current_point  # Store parent reference
                    stack.append(neighbor)

    return visited_points, attempt_stack


def search_A_start(maze: list, root_point: tuple[int, int], visited_points: list):
    # TODO: to be implemented
    stack: list = []
    stack.append(root_point)
    goal_point, roadblocks, boundaries = maze
    parent_map = {}  # Dictionary to store parent relationships
    cost_of_movement: list = []
    while stack:
        current_point = stack.pop()
        if current_point not in visited_points:
            visited_points.append(current_point)
            if current_point == goal_point:
                print(parent_map)  # Store parent reference
                return visited_points
            else:
                neighbors = _get_neighbors(current_point, roadblocks, boundaries)
                for neighbor in neighbors:
                    parent_map[neighbor] = current_point  # Store parent reference
                    cost_of_movement.append(_calculate_cost(current_point, neighbor))
                    stack.append(neighbor)
                stack = [stack for stack, _ in sorted(zip(stack, cost_of_movement))]

    return "no path to goal"
