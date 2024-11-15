import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from agent import Agent

class HillClimbingAgent(Agent):
    def hill_climbing(self):
        '''Performs Hill Climbing search on the maze and returns the path.'''
        start_time = time.time()
        
        current_position = self.maze.start
        self.reset_visited()
        self.visited[current_position[0]][current_position[1]] = True
        path = [current_position]  # Initialize the path with the start position
        
        # Calculate Manhattan distance
        def heuristic(position):
            x, y = position
            goal_x, goal_y = self.maze.goal
            return abs(x - goal_x) + abs(y - goal_y)
        
        while True:
            x, y = current_position
            # Check if we've reached the goal
            if current_position == self.maze.goal:
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"Hill Climbing execution time: {execution_time:.6f} seconds")
                return path  # Return the path to the goal

            # Generate neighbors
            neighbors = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                    neighbors.append((nx, ny))
                    self.visited[nx][ny] = True

            # No more neighbors to explore
            if not neighbors:
                break

            # Find the neighbor with the minimum heuristic
            next_position = min(neighbors, key=heuristic)

            # Stop if no better neighbor is found
            if heuristic(next_position) >= heuristic(current_position):
                break
            
            # Move to the better neighbor
            current_position = next_position
            path.append(current_position)
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Hill Climbing execution time: {execution_time:.6f} seconds")
        print("Local maximum reached; no path found to goal.")
        
        return path