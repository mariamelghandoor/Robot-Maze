import os
import sys
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
from agent import Agent

class FirstChoiceHillClimbingAgent(Agent):
    def first_choice_hill_climbing(self):
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
                print(f"First-Choice Hill Climbing execution time: {execution_time:.6f} seconds")
                print(f"Peak Memory Usage in First-Choice Hill Climbing: {peak / 1024/ 1024:.2f} MB")
                return path

            # Generate neighbors and shuffle them to introduce randomness
            neighbors = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                    neighbors.append((nx, ny))
            
            random.shuffle(neighbors)  # Randomize neighbor order for first-choice
            
            found_better = False
            for neighbor in neighbors:
                if heuristic(neighbor) < heuristic(current_position):  # First better neighbor
                    current_position = neighbor
                    path.append(current_position)
                    self.visited[current_position[0]][current_position[1]] = True
                    found_better = True
                    break
            
            # Stop if no better neighbor is found
            if not found_better:
                break
        
        end_time = time.time()
        execution_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"First-Choice Hill Climbing execution time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage in First-Choice Hill Climbing: {peak / 1024/ 1024:.2f} MB")
        print("Local maximum reached; no path found to goal.")
        
        return path