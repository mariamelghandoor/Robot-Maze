import numpy as np
import matplotlib.pyplot as plt

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = (0, 0)  # Starting point
        self.goal = (self.height - 1, self.width - 1)  # Goal point

    def is_open(self, x, y):
        in_bounds = 0 <= x < self.height and 0 <= y < self.width
        cell_is_open = self.grid[x][y] == 0 if in_bounds else False
        return in_bounds and cell_is_open

    def plot(self, path, method_name):
        maze_array = np.array(self.grid)

        plt.figure(figsize=(10, 10))
        cmap = plt.get_cmap('binary')
        plt.imshow(maze_array, cmap=cmap)

        if path:
            # Extract x and y coordinates from the path
            path_x = [coord[0] for coord in path]  # Row
            path_y = [coord[1] for coord in path]  # Column

            plt.plot(path_y, path_x, label=f'{method_name} Path', linewidth=2, marker='o', markersize=6)

        plt.scatter(self.start[1], self.start[0], color='green', label='Start', s=200, marker='o')
        plt.scatter(self.goal[1], self.goal[0], color='red', label='Goal', s=200, marker='x')

        plt.grid(which='both', color='black', linestyle='-', linewidth=1)
        plt.xticks(np.arange(-0.5, self.width, 1), [])
        plt.yticks(np.arange(-0.5, self.height, 1), [])
        plt.gca().set_xticks(np.arange(0.5, self.width, 1), minor=True)
        plt.gca().set_yticks(np.arange(0.5, self.height, 1), minor=True)
        plt.grid(True, which='minor', color='black', linestyle='-', linewidth=2)

        plt.legend(loc='upper right')
        plt.title(f'Maze Visualization with {method_name} Path', fontsize=16)

        plt.show()
