import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from queue import Queue
from agent import Agent

class BFSAgent(Agent):
    def bfs(self):
        start_time = time.time()
        
        queue = Queue()
        queue.put([self.maze.start])
        self.reset_visited()
        self.visited[self.maze.start[0]][self.maze.start[1]] = True

        while not queue.empty():
            path = queue.get()
            x, y = path[-1]
            
            # Check goal
            if (x, y) == self.maze.goal:

                end_time = time.time()
                execution_time = end_time - start_time
                print(f"BFS execution time: {execution_time:.6f} seconds")
                
                return path
            
            # Explore neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:  # Check valid and not visited
                    self.visited[nx][ny] = True
                    new_path = list(path) + [(nx, ny)]
                    queue.put(new_path)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"BFS execution time: {execution_time:.6f} seconds")

        print("No path found from start to goal.")
        return None 
