from maze_generator import create_maze, plot_maze
from algorithms import search_bfs


def main(maze_size: int, roadblocks: int):
    xx, yy, start_point, goal_point, block_points = create_maze(
        maze_dim=maze_size, blocked_positions=roadblocks
    )
    visited_points: list = []
    print(f"{start_point}, {goal_point}")
    path_to_goal = search_bfs([xx, yy, goal_point, block_points], start_point, visited_points)
    print(path_to_goal)
    _, fig = plot_maze(xx, yy, start_point, goal_point, block_points, plot_result=path_to_goal)
    fig.savefig("final_result")


if __name__ == "__main__":
    maze_size = 6
    road_blocks = 3
    main(maze_size, road_blocks)
