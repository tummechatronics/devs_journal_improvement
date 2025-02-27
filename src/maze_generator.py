import numpy as np
import matplotlib.pyplot as plt


def create_maze(
    maze_dim: int, *, blocked_positions: int = 1
) -> tuple[np.array, np.array, tuple[int, int], tuple[int, int], list[tuple[int, int]]]:
    """Create an NxN maze with possible blocked positions

    Args:
        maze_dim (int): _description_
        blocked_positions (int, optional): _description_. Defaults to 1.

    Returns:
        tuple[maze_x_length,maze_y_length,tuple(random_start_point_xy),tuple(random_goal_point_xy),
        random_blocks_point_flat_xy,]
    """

    rng = np.random.default_rng()
    #! we are creating points without checking if start,goal and block are the same point
    # TODO: move out point generation out of the maze_creation method and set a guard to avoid problems with the points
    random_start_point_xy, random_goal_point_xy = rng.integers(maze_dim, size=(2, 2))
    random_blocks_point_xy = rng.integers(maze_dim, size=(2, blocked_positions))
    random_blocks_point_flat_xy = [(x, y) for x, y in zip(random_blocks_point_xy[0], random_blocks_point_xy[1])]
    maze_length = np.arange(maze_dim, step=1)

    maze_x_length, maze_y_length = np.meshgrid(maze_length, maze_length, indexing="xy")

    return (
        maze_x_length,
        maze_y_length,
        tuple(random_start_point_xy),
        tuple(random_goal_point_xy),
        random_blocks_point_flat_xy,
    )


def plot_maze(
    maze_x_length: np.array,
    maze_y_length: np.array,
    random_start_point_xy: tuple[int, int],
    random_goal_point_xy: tuple[int, int],
    random_blocks_point_flat_xy: list[tuple[int, int]],
    *,
    plot_result: list[tuple[int, int]] = None,
):
    fig, ax = plt.subplots()
    # TODO: Improve the layout
    ax.grid(True, which="both")
    plt.axis([-0.5, maze_x_length.max() + 1, -0.5, maze_y_length.max() + 1])
    plt.plot(maze_x_length, maze_y_length, marker=".", color="w", linestyle="none")
    if plot_result:
        plt.plot(*zip(*plot_result), marker="*", color="b")
    plt.plot(*random_start_point_xy, marker="*", color="b")
    plt.plot(*random_goal_point_xy, marker="s", color="r")
    plt.plot(*zip(*random_blocks_point_flat_xy), marker="X", color="k", linestyle="none")
    return plt, fig


if __name__ == "__main__":
    maze_size = 6
    xx, yy, start_point, goal_point, block_points = create_maze(maze_size, blocked_positions=int(maze_size / 2))
    # Example usage
    plot_maze(xx, yy, start_point, goal_point, block_points)
