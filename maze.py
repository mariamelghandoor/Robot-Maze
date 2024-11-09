
import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
class Colors:
    red = '\033[91m'
    yellow = '\033[93m'
    purple = '\033[95m'
    reset = '\033[0m'

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = (0, 0)  # Starting point
        self.goal = (self.height - 1, self.width - 1)  # Goal point

    def is_open(self, x, y):
        in_bounds = 0 <= x < self.height and 0 <= y < self.width
        cell_is_open = self.grid[x][y] != 1 if in_bounds else False
        return in_bounds and cell_is_open
    
    def __getitem__(self, item):
        x, y = item
        return self.grid[x][y]

    def plot(self, path, method_name):
        maze_array = np.array(self.grid)
        maze_array_cost = copy.deepcopy(maze_array)
        plt.figure(figsize=(10, 10))
        maze_array = np.where(maze_array == 1, 1, 0)
        cmap = plt.get_cmap('binary')
        plt.imshow(maze_array, cmap=cmap)

        if path:
            # Extract x and y coordinates from the path
            if type(path[0]) == int:
                path_x = [coord[0] for coord in path[1]]  # Row
                path_y = [coord[1] for coord in path[1]]  # Column
                cost = [maze_array_cost[coord[0]][coord[1]] for coord in path[1]]
            else:
                path_x = [coord[0] for coord in path]  # Row
                path_y = [coord[1] for coord in path]  # Column
                cost = [maze_array_cost[coord[0]][coord[1]] for coord in path]
          
            Total = sum(cost)
            
            print('\n')

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
        plt.title(f'Maze Visualization with {method_name} Path with Total Cost {Total}', fontsize=16)

        plt.show()

    def print_maze(self, path=None):
        path_set = set(path) if path else set()
        print("██" * (self.width + 2)) 
        
        for i, row in enumerate(self.grid):
            print("██", end='')
            
            for j, cell in enumerate(row):
                pos = (i, j)
                
                if pos == self.start:
                    print(" S", end='')
                elif pos == self.goal:
                    print(" G", end='')
                elif pos in path_set:
                    print("❤️", end='') 
                elif cell == 1:
                    print("  ", end='')
                elif cell == 0:
                    print("██", end='')
            
            print("██")
        print("██" * (self.width + 2))

