import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def create_maze(maze_dim: int, *, blocked_positions: int = 0) -> tuple[np.ndarray, np.ndarray]:
    """Create an NxN maze with possible blocked positions

    Args:
        maze_dim (int): _description_
        blocked_positions (int, optional): _description_. Defaults to 0.

    Returns:
        tuple[np.ndarray, np.ndarray]: _description_
    """

    maze_length = np.arange(maze_dim**2, dtype=np.int64)

    maze_x_length, maze_y_length = np.meshgrid(maze_length, maze_length)

    return maze_x_length, maze_y_length


def plot_maze(maze_dim: int, *, blocked_positions: int = 0):
    fig, ax = plt.subplots()
    step_size = 1
    ax.grid(True, which="both", linestyle="-", linewidth=0.5)
    ax.set_xticks(range(0, maze_dim + 1, step_size))
    ax.set_yticks(range(0, maze_dim + 1, step_size))
    plt.axis([0, maze_dim, 0, maze_dim])
    print(plt.axis)
    plt.show()


def draw_grid(maze_x_length: int, maze_y_length: int, step_count):
    image = Image.new(mode="L", size=(maze_x_length, maze_y_length), color=255)
    draw = ImageDraw.Draw(image)
    step_size = maze_x_length // step_count
    for x in range(0, maze_x_length, step_size):
        draw.line([(x, 0), (x, maze_y_length)], fill=128)
    for y in range(0, maze_y_length, step_size):
        draw.line([(0, y), (maze_x_length, y)], fill=128)
    del draw
    return image


if __name__ == "__main__":
    xx, yy = create_maze(6)
    # Example usage
    plot_maze(6)
    # grid_image = draw_grid(600, 600, 6)
    # grid_image.show()
