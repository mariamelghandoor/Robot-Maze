import math
import random
from agent import Agent
from collections import OrderedDict

class Simulated(Agent):
    def get_neighbor(self, x, y):
        neighbors = {}
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                neighbors[(nx, ny)] = self.maze[nx, ny] - self.maze[x, y]
                self.visited[nx][ny] = True  # Mark as visited here
        print(f"Inside the neighbor function: {neighbors}")
        return neighbors

    def simulated_annealing(self, n_iterations=1000, temp=10):
        # Initial solution
        x, y = self.maze.start  # Assuming (0, 0)
        path = [(x, y)]
        self.visited[0][0] = True

        # Stack for backtracking, storing (x, y, sorted_neighbors)
        stack = []

        for i in range(n_iterations):
            # Decrease temperature
            t = temp / float(i + 1)

            # Get neighbors
            neighbors = self.get_neighbor(x, y)
            print(f"neighbors from get_neighbor {neighbors}")
            if not neighbors:
                # No neighbors, we need to backtrack
                print("Dead end reached. Backtracking...")
                if not stack:
                    print("No more states to backtrack to. Stopping.")
                    return path  # No path found
                # Backtrack to the previous state
                x, y, sorted_neighbors = stack.pop()
                print(f"neighbors sorted {sorted_neighbors}")
                if sorted_neighbors:
                    first_key = next(iter(sorted_neighbors))
                    x, y = first_key
                    print((x, y))
                continue

            # Sort and add current neighbors to stack
            sorted_neighbors = OrderedDict(sorted(neighbors.items(), key=lambda item: item[1]))
            stack.append((x, y, sorted_neighbors))
            print(f"stack: {stack}")
            # Choose the lowest-cost neighbor and remove from stack's top state
            minimum_pos, minimum_cost = sorted_neighbors.popitem(last=False)

            # Check if we should accept the new state
            if minimum_cost < 0 or random.random() < math.exp(-minimum_cost / t):
                x, y = minimum_pos
                path.append((x, y))
                # Stop if the goal is reached
                if (x, y) == self.maze.goal:
                    print("Goal reached!")
                    return path

            # Optional: Print progress
            if i % 100 == 0:
                print(f"Iteration {i}, Temperature {t:.3f}")

        print("Maximum iterations reached.")
        return path
