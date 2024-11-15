import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
from agent import Agent

class SteepestAscentHillClimbingAgent(Agent):
    def steepest_ascent_hill_climbing(self):
        tracemalloc.start()
        start_time = time.time()
        
        current_position = self.maze.start
        self.reset_visited()
        self.visited[current_position[0]][current_position[1]] = True
        path = [current_position]
        
        # Manhattan distance
        def heuristic(position):
            x, y = position
            goal_x, goal_y = self.maze.goal
            return abs(x - goal_x) + abs(y - goal_y)
        
        while True:
            x, y = current_position
            if current_position == self.maze.goal:
                end_time = time.time()
                execution_time = end_time - start_time
                current, peak = tracemalloc.get_traced_memory()
                print(f"Steepest-Ascent Hill Climbing execution time: {execution_time:.6f} seconds")
                print(f"Peak Memory Usage in Steepest-Ascent Hill Climbing: {peak / 1024 / 1024:.2f} MB")
                return path

            # Generate neighbors
            neighbors = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                    neighbors.append((nx, ny))
                    self.visited[nx][ny] = True

            if not neighbors:
                break

            # Find the neighbor with the steepest descent in heuristic
            next_position = min(neighbors, key=heuristic, default=None)

            # Stop if no better neighbor is found
            if next_position is None or heuristic(next_position) >= heuristic(current_position):
                break

            # Move to the best neighbor
            current_position = next_position
            path.append(current_position)
        
        end_time = time.time()
        execution_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"Steepest-Ascent Hill Climbing execution time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage in Steepest-Ascent Hill Climbing: {peak / 1024 / 1024:.2f} MB")
        print("Local maximum reached; no path found to goal.")
        
        return path