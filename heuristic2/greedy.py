import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
from queue import PriorityQueue
from agent import Agent

class GreedyAgent2(Agent):     
    #  Euclidean distance
    def heuristic(self, x, y):
        goal_x, goal_y = self.maze.goal
        return ((x - goal_x) ** 2 + (y - goal_y) ** 2) ** 0.5

    def greedy(self):    
        tracemalloc.start()
        start_time = time.time()
        pq = PriorityQueue()
        pq.put((0, [self.maze.start]))
        self.reset_visited()
        self.visited[self.maze.start[0]][self.maze.start[1]] = True

        while not pq.empty():
            _, path = pq.get()
            x, y = path[-1]
            
            if (x, y) == self.maze.goal:
                end_time = time.time()
                execution_time = end_time - start_time
                current, peak = tracemalloc.get_traced_memory()
                print(f"Greedy search execution time: {execution_time:.6f} seconds")
                print(f"Peak Memory Usage in Greedy: {peak / 1024/ 1024:.2f} MB")
                return path
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                    self.visited[nx][ny] = True
                    new_path = list(path) + [(nx, ny)]
                    heuristic_value = self.heuristic(nx, ny)
                    pq.put((heuristic_value, new_path))

        end_time = time.time()
        execution_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"Greedy search execution time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage: {peak / 1024/ 1024:.2f} MB")
        print("No path found from start to goal.")
        return None
