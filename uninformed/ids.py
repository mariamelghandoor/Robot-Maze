import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
from agent import Agent

class IDSAgent(Agent):
    def ids(self, max_depth = 1000000000):
        tracemalloc.start()
        start_time = time.time()
        for depth in range(max_depth + 1):
            self.reset_visited()
            res = self.depth_limit([self.maze.start], depth)
            if res:
                end_time = time.time()
                execution_time = end_time - start_time
                current, peak = tracemalloc.get_traced_memory()
                print(f"IDS execution time: {execution_time:.6f} seconds")
                print(f"Peak Memory Usage in IDS: {peak / 1024/ 1024:.2f} MB")
                return res
        
        end_time = time.time()
        execution_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"IDS execution time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage in IDS: {peak/ 1024/ 1024:.2f} MB")
        print("No path found within the maximum depth limit")
        return None
    
    def depth_limit(self, path, limit):
        x, y = path[-1]
        if (x, y) == self.maze.goal:
            return path
        
        if limit <= 0:
            return None
        self.visited[x][y] = True

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                new_path = list(path)
                new_path.append((nx, ny))

                res = self.depth_limit(new_path, limit - 1)
                if res:
                    return res

        return None

