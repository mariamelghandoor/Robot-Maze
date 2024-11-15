import math
import time
import random
import tracemalloc
from collections import OrderedDict

class Simulated:
    def __init__(self, maze):
        self.maze = maze
        self.visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]

    def get_neighbor(self, x, y):
        neighbors = {}
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                neighbors[(nx, ny)] = self.maze[nx, ny] - self.maze[x, y]
        return neighbors

    def simulated_annealing(self, n_iterations=1000, temp=10000, max_restarts=3):
        # Initialize start point and path
        tracemalloc.start()
        start_time = time.time()
        x, y = self.maze.start
        path = [(x, y)]
        self.visited[x][y] = True
        restarts = 0

        for i in range(n_iterations):
            # Decrease temperature
            t = temp / float(i + 1)

            # Get neighbors
            neighbors = self.get_neighbor(x, y)
            
            # If no neighbors available, try to backtrack
            if not neighbors:
                if len(path) > 1:
                    path.pop()  # Remove the current dead-end position
                    x, y = path[-1]  # Go back to the previous position
                    continue
                else:
                    # If backtracking fails (at start), restart
                    if restarts < max_restarts:
                        restarts += 1
                        x, y = self.maze.start
                        path = [(x, y)]
                        self.visited = [[False for _ in range(self.maze.width)] for _ in range(self.maze.height)]
                        self.visited[x][y] = True
                        continue
                    else:
                        # Return path if max restarts reached
                        return path

            # Sort neighbors by cost difference
            sorted_neighbors = OrderedDict(sorted(neighbors.items(), key=lambda item: item[1]))
            minimum_pos, minimum_cost = sorted_neighbors.popitem(last=False)

            # Decide whether to accept the new position based on temperature
            if minimum_cost < 0 or random.random() < math.exp(-minimum_cost / t):
                x, y = minimum_pos
                path.append((x, y))
                self.visited[x][y] = True

                # Stop if the goal is reached
                if (x, y) == self.maze.goal:
                    end_time = time.time()
                    execution_time = end_time - start_time
                    current, peak = tracemalloc.get_traced_memory()
                    print(f"Simulated Annealing execution time: {execution_time:.6f} seconds")
                    print(f"Peak Memory Usage in Simulated Annealing: {peak / 1024 / 1024:.2f} MB")
                    return path  # Return only the final path once the goal is reached

        # Return the path as it stands if iterations run out
        end_time = time.time()
        execution_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"Simulated Annealing execution time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage in Simulated Annealing: {peak / 1024 / 1024:.2f} MB")
        return path