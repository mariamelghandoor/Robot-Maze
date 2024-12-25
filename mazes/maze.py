
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

    def is_open_Qlearning(self, x, y):
        # print(type(self.grid[x][y]))
        # print('self.grid[x][y] ', self.grid[x][y], 'grid[x][y] != None', self.grid[x][y] != None)
        return self.grid[x][y] != 'None'
    
    def __getitem__(self, item):
        x, y = item
        return self.grid[x][y]

    def plot_Qlearning(self, path, method_name):
        maze_array = np.array(self.grid)
        print(maze_array)
        maze_array_cost = copy.deepcopy(maze_array)

        # Initialize visualization array
        maze_visual = np.zeros_like(maze_array, dtype=int)  # All open paths initially

        # Assign values for each cell type
        maze_visual[maze_array == 'None'] = 0    # Obstacle (black)
        maze_visual[maze_array == '-1'] = 1       # Hole (blue)
        maze_visual[maze_array == '-0.04'] = 2        # Open cell (white)

        plt.figure(figsize=(10, 10))

        # Use a colormap for non-obstacle cells
        cmap = plt.cm.get_cmap('coolwarm', 3)  # Get a colormap with 3 discrete colors

        # Create a custom color array using RGB colors directly for each cell type
        maze_colors = np.ones((maze_visual.shape[0], maze_visual.shape[1], 3))  # Default to white
        
        # Map the values to RGB
        maze_colors[maze_visual == 0] = [0, 0, 0]  # Obstacle (black)
        maze_colors[maze_visual == 1] = [0, 0, 1]  # Hole (blue)
        maze_colors[maze_visual == 2] = [1, 1, 1]  # Open path (white)

        plt.imshow(maze_colors)

        if path:
            # Extract x and y coordinates from the path
            path_x = [coord[0] for coord in path]  # Row
            path_y = [coord[1] for coord in path]  # Column
            cost = [maze_array_cost[coord[0]][coord[1]] for coord in path]
            Total = sum([int(float(value)) for value in cost])
            Total = "{:,}".format(Total)
            
            plt.plot(path_y, path_x, label=f'{method_name} Path', linewidth=2, marker='o', markersize=6)

        # Plot start and goal points
        plt.scatter(self.start[1], self.start[0], color='green', label='Start', s=200, marker='o')
        plt.scatter(self.goal[1], self.goal[0], color='red', label='Goal', s=200, marker='x')

        # Configure the grid
        plt.grid(which='both', color='black', linestyle='-', linewidth=1)
        plt.xticks(np.arange(-0.5, self.width, 1), [])
        plt.yticks(np.arange(-0.5, self.height, 1), [])
        plt.gca().set_xticks(np.arange(0.5, self.width, 1), minor=True)
        plt.gca().set_yticks(np.arange(0.5, self.height, 1), minor=True)
        plt.grid(True, which='minor', color='black', linestyle='-', linewidth=2)

        # Add legend and title
        plt.legend(loc='upper right')
        plt.title(f'Maze Visualization with {method_name} ', fontsize=16)

        plt.show()

    def plot(self, path, method_name):
        maze_array = np.array(self.grid)
        maze_array_cost = copy.deepcopy(maze_array)
        plt.figure(figsize=(10, 10))
        maze_array = np.where(maze_array == 1, 1, 0)
        cmap = plt.get_cmap('binary')
        plt.imshow(maze_array, cmap=cmap)

        if path:
            # Extract x and y coordinates from the path
            path_x = [coord[0] for coord in path]  # Row
            path_y = [coord[1] for coord in path]  # Column
            cost = [maze_array_cost[coord[0]][coord[1]] for coord in path]
            Total = sum([int(float(value)) for value in cost])
            Total = "{:,}".format(Total)
            
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

