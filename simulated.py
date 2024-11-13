import math
import random
from agent import Agent

class Simulated(Agent):
    def get_neighbor(self, x, y, step_size=0.1):
        neighbors = {}
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.maze.is_open(nx, ny):
                neighbors[(nx, ny)] = self.maze[nx, ny]
        return neighbors

    def choose_cost(self, current_cost, neighbors):
        minimum = float('inf')
        for pos, cost in neighbors.items():
            if cost - current_cost < minimum:
                minimum = cost - current_cost
            
    # Simulated Annealing function
    def simulated_annealing(self, path, bounds, n_iterations, step_size, temp):
        # Initial solution
        x, y = path[-1]
        for i in range(n_iterations):
            # Decrease temperature
            t = temp / float(i + 1)
            # Generate candidate solution
            candidate = self.get_neighbor(x, y, step_size)
            
            # Check if we should keep the new solution
            if candidate_eval < best_eval or random.random() < math.exp((current_eval - candidate_eval) / t):
                current, current_eval = candidate, candidate_eval
                if candidate_eval < best_eval:
                    best, best_eval = candidate, candidate_eval
                    scores.append(best_eval)

            # Optional: print progress
            if i % 100 == 0:
                print(f"Iteration {i}, Temperature {t:.3f}, Best Evaluation {best_eval:.5f}")

        return best, best_eval, scores

# Define problem domain
bounds = [(-5.0, 5.0) for _ in range(2)]  # for a 2-dimensional Rastrigin function
n_iterations = 1000
step_size = 0.1
temp = 10
