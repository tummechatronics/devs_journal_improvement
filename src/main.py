from maze_generator import create_maze, plot_maze
from algorithms import search_bfs, search_dfs


def main(maze_size: int, roadblocks: int):
    xx, yy, start_point, goal_point, block_points, boundaries = create_maze(
        maze_dim=maze_size, blocked_positions=roadblocks
    )
    visited_points: list = []
    print(f"{start_point}, {goal_point}")
    path_to_goal_bfs = search_bfs([goal_point, block_points, boundaries], start_point, visited_points)
    path_to_goal_dfs, _ = search_dfs([goal_point, block_points, boundaries], start_point, visited_points)
    i = 0
    for path_to_goal in [path_to_goal_bfs, path_to_goal_dfs]:
        print(f"{path_to_goal}")
        plt, fig = plot_maze(xx, yy, start_point, goal_point, block_points, plot_result=path_to_goal)
        fig.savefig(f"final_result_{i}")
        plt.show()
        i += 1


if __name__ == "__main__":
    maze_size = 6
    road_blocks = 3
    main(maze_size, road_blocks)
